#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates label detection on a demo video using
the Google Cloud API.

Usage:
    python quickstart.py

"""


def run_quickstart():
    # [START video_quickstart]
    from google.cloud import videointelligence

    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]
    operation = video_client.annotate_video(
        "gs://cloud-samples-data/video/cat.mp4", features=features
    )
    print("\nProcessing video for label annotations:")

    result = operation.result(timeout=120)
    print("\nFinished processing.")

    # first result is retrieved because a single video was processed
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print(f"Video label description: {segment_label.entity.description}")
        for category_entity in segment_label.category_entities:
            print(f"\tLabel category description: {category_entity.description}")

        for i, segment in enumerate(segment_label.segments):
            start_time = (
                segment.segment.start_time_offset.seconds
                + segment.segment.start_time_offset.nanos / 1e9
            )
            end_time = (
                segment.segment.end_time_offset.seconds
                + segment.segment.end_time_offset.nanos / 1e9
            )
            positions = f"{start_time}s to {end_time}s"
            confidence = segment.confidence
            print(f"\tSegment {i}: {positions}")
            print(f"\tConfidence: {confidence}")
        print("\n")
    # [END video_quickstart]


if __name__ == "__main__":
    run_quickstart()