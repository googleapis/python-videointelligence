# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START video_detect_faces]
import io

from google.cloud import videointelligence_v1 as videointelligence


def detect_faces(local_file_path="path/to/your/video-file.mp4"):
    """Detects faces in a video from a local file."""

    client = videointelligence.VideoIntelligenceServiceClient()

    with io.open(local_file_path, "rb") as f:
        input_content = f.read()

    # Configure the request
    config = videointelligence.FaceDetectionConfig(
        include_bounding_boxes=True, include_attributes=True
    )
    context = videointelligence.VideoContext(face_detection_config=config)

    # Start the asynchronous request
    operation = client.annotate_video(
        request={
            "features": [videointelligence.Feature.FACE_DETECTION],
            "input_content": input_content,
            "video_context": context,
        }
    )

    print("\nProcessing video for face detection annotations.")
    result = operation.result(timeout=300)

    print("\nFinished processing.\n")

    # Retrieve the first result, because a single video was processed.
    annotation_result = result.annotation_results[0]

    for annotation in annotation_result.face_detection_annotations:
        print("Face detected:")
        for track in annotation.tracks:
            print(
                "Segment: {}s to {}s".format(
                    track.segment.start_time_offset.seconds
                    + track.segment.start_time_offset.microseconds / 1e6,
                    track.segment.end_time_offset.seconds
                    + track.segment.end_time_offset.microseconds / 1e6,
                )
            )

            # Each segment includes timestamped faces that include
            # characteristics of the face detected.
            # Grab the first timestamped face
            timestamped_object = track.timestamped_objects[0]
            box = timestamped_object.normalized_bounding_box
            print("Bounding box:")
            print("\tleft  : {}".format(box.left))
            print("\ttop   : {}".format(box.top))
            print("\tright : {}".format(box.right))
            print("\tbottom: {}".format(box.bottom))

            # Attributes include glasses, headwear, smiling, direction of gaze
            print("Attributes:")
            for attribute in timestamped_object.attributes:
                print(
                    "\t{}:{} {}".format(
                        attribute.name, attribute.value, attribute.confidence
                    )
                )


# [END video_detect_faces]
