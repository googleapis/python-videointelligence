# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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
#

import proto  # type: ignore


from google.protobuf import duration_pb2 as duration  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.videointelligence.v1p3beta1",
    manifest={
        "LabelDetectionMode",
        "Likelihood",
        "StreamingFeature",
        "Feature",
        "AnnotateVideoRequest",
        "VideoContext",
        "LabelDetectionConfig",
        "ShotChangeDetectionConfig",
        "ObjectTrackingConfig",
        "ExplicitContentDetectionConfig",
        "FaceDetectionConfig",
        "PersonDetectionConfig",
        "TextDetectionConfig",
        "VideoSegment",
        "LabelSegment",
        "LabelFrame",
        "Entity",
        "LabelAnnotation",
        "ExplicitContentFrame",
        "ExplicitContentAnnotation",
        "NormalizedBoundingBox",
        "TimestampedObject",
        "Track",
        "DetectedAttribute",
        "Celebrity",
        "CelebrityTrack",
        "CelebrityRecognitionAnnotation",
        "DetectedLandmark",
        "FaceDetectionAnnotation",
        "PersonDetectionAnnotation",
        "VideoAnnotationResults",
        "AnnotateVideoResponse",
        "VideoAnnotationProgress",
        "AnnotateVideoProgress",
        "SpeechTranscriptionConfig",
        "SpeechContext",
        "SpeechTranscription",
        "SpeechRecognitionAlternative",
        "WordInfo",
        "NormalizedVertex",
        "NormalizedBoundingPoly",
        "TextSegment",
        "TextFrame",
        "TextAnnotation",
        "ObjectTrackingFrame",
        "ObjectTrackingAnnotation",
        "LogoRecognitionAnnotation",
        "StreamingAnnotateVideoRequest",
        "StreamingVideoConfig",
        "StreamingAnnotateVideoResponse",
        "StreamingVideoAnnotationResults",
        "StreamingShotChangeDetectionConfig",
        "StreamingLabelDetectionConfig",
        "StreamingExplicitContentDetectionConfig",
        "StreamingObjectTrackingConfig",
        "StreamingAutomlActionRecognitionConfig",
        "StreamingAutomlClassificationConfig",
        "StreamingAutomlObjectTrackingConfig",
        "StreamingStorageConfig",
    },
)


class LabelDetectionMode(proto.Enum):
    r"""Label detection mode."""
    LABEL_DETECTION_MODE_UNSPECIFIED = 0
    SHOT_MODE = 1
    FRAME_MODE = 2
    SHOT_AND_FRAME_MODE = 3


class Likelihood(proto.Enum):
    r"""Bucketized representation of likelihood."""
    LIKELIHOOD_UNSPECIFIED = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5


class StreamingFeature(proto.Enum):
    r"""Streaming video annotation feature."""
    STREAMING_FEATURE_UNSPECIFIED = 0
    STREAMING_LABEL_DETECTION = 1
    STREAMING_SHOT_CHANGE_DETECTION = 2
    STREAMING_EXPLICIT_CONTENT_DETECTION = 3
    STREAMING_OBJECT_TRACKING = 4
    STREAMING_AUTOML_ACTION_RECOGNITION = 23
    STREAMING_AUTOML_CLASSIFICATION = 21
    STREAMING_AUTOML_OBJECT_TRACKING = 22


class Feature(proto.Enum):
    r"""Video annotation feature."""
    FEATURE_UNSPECIFIED = 0
    LABEL_DETECTION = 1
    SHOT_CHANGE_DETECTION = 2
    EXPLICIT_CONTENT_DETECTION = 3
    FACE_DETECTION = 4
    SPEECH_TRANSCRIPTION = 6
    TEXT_DETECTION = 7
    OBJECT_TRACKING = 9
    LOGO_RECOGNITION = 12
    CELEBRITY_RECOGNITION = 13
    PERSON_DETECTION = 14


class AnnotateVideoRequest(proto.Message):
    r"""Video annotation request.

    Attributes:
        input_uri (str):
            Input video location. Currently, only `Cloud
            Storage <https://cloud.google.com/storage/>`__ URIs are
            supported. URIs must be specified in the following format:
            ``gs://bucket-id/object-id`` (other URI formats return
            [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]).
            For more information, see `Request
            URIs <https://cloud.google.com/storage/docs/request-endpoints>`__.
            To identify multiple videos, a video URI may include
            wildcards in the ``object-id``. Supported wildcards: '*' to
            match 0 or more characters; '?' to match 1 character. If
            unset, the input video should be embedded in the request as
            ``input_content``. If set, ``input_content`` must be unset.
        input_content (bytes):
            The video data bytes. If unset, the input video(s) should be
            specified via the ``input_uri``. If set, ``input_uri`` must
            be unset.
        features (Sequence[~.video_intelligence.Feature]):
            Required. Requested video annotation
            features.
        video_context (~.video_intelligence.VideoContext):
            Additional video context and/or feature-
            pecific parameters.
        output_uri (str):
            Optional. Location where the output (in JSON format) should
            be stored. Currently, only `Cloud
            Storage <https://cloud.google.com/storage/>`__ URIs are
            supported. These must be specified in the following format:
            ``gs://bucket-id/object-id`` (other URI formats return
            [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]).
            For more information, see `Request
            URIs <https://cloud.google.com/storage/docs/request-endpoints>`__.
        location_id (str):
            Optional. Cloud region where annotation should take place.
            Supported cloud regions are: ``us-east1``, ``us-west1``,
            ``europe-west1``, ``asia-east1``. If no region is specified,
            the region will be determined based on video file location.
    """

    input_uri = proto.Field(proto.STRING, number=1)

    input_content = proto.Field(proto.BYTES, number=6)

    features = proto.RepeatedField(proto.ENUM, number=2, enum="Feature",)

    video_context = proto.Field(proto.MESSAGE, number=3, message="VideoContext",)

    output_uri = proto.Field(proto.STRING, number=4)

    location_id = proto.Field(proto.STRING, number=5)


class VideoContext(proto.Message):
    r"""Video context and/or feature-specific parameters.

    Attributes:
        segments (Sequence[~.video_intelligence.VideoSegment]):
            Video segments to annotate. The segments may
            overlap and are not required to be contiguous or
            span the whole video. If unspecified, each video
            is treated as a single segment.
        label_detection_config (~.video_intelligence.LabelDetectionConfig):
            Config for LABEL_DETECTION.
        shot_change_detection_config (~.video_intelligence.ShotChangeDetectionConfig):
            Config for SHOT_CHANGE_DETECTION.
        explicit_content_detection_config (~.video_intelligence.ExplicitContentDetectionConfig):
            Config for EXPLICIT_CONTENT_DETECTION.
        face_detection_config (~.video_intelligence.FaceDetectionConfig):
            Config for FACE_DETECTION.
        speech_transcription_config (~.video_intelligence.SpeechTranscriptionConfig):
            Config for SPEECH_TRANSCRIPTION.
        text_detection_config (~.video_intelligence.TextDetectionConfig):
            Config for TEXT_DETECTION.
        person_detection_config (~.video_intelligence.PersonDetectionConfig):
            Config for PERSON_DETECTION.
        object_tracking_config (~.video_intelligence.ObjectTrackingConfig):
            Config for OBJECT_TRACKING.
    """

    segments = proto.RepeatedField(proto.MESSAGE, number=1, message="VideoSegment",)

    label_detection_config = proto.Field(
        proto.MESSAGE, number=2, message="LabelDetectionConfig",
    )

    shot_change_detection_config = proto.Field(
        proto.MESSAGE, number=3, message="ShotChangeDetectionConfig",
    )

    explicit_content_detection_config = proto.Field(
        proto.MESSAGE, number=4, message="ExplicitContentDetectionConfig",
    )

    face_detection_config = proto.Field(
        proto.MESSAGE, number=5, message="FaceDetectionConfig",
    )

    speech_transcription_config = proto.Field(
        proto.MESSAGE, number=6, message="SpeechTranscriptionConfig",
    )

    text_detection_config = proto.Field(
        proto.MESSAGE, number=8, message="TextDetectionConfig",
    )

    person_detection_config = proto.Field(
        proto.MESSAGE, number=11, message="PersonDetectionConfig",
    )

    object_tracking_config = proto.Field(
        proto.MESSAGE, number=13, message="ObjectTrackingConfig",
    )


class LabelDetectionConfig(proto.Message):
    r"""Config for LABEL_DETECTION.

    Attributes:
        label_detection_mode (~.video_intelligence.LabelDetectionMode):
            What labels should be detected with LABEL_DETECTION, in
            addition to video-level labels or segment-level labels. If
            unspecified, defaults to ``SHOT_MODE``.
        stationary_camera (bool):
            Whether the video has been shot from a stationary (i.e.,
            non-moving) camera. When set to true, might improve
            detection accuracy for moving objects. Should be used with
            ``SHOT_AND_FRAME_MODE`` enabled.
        model (str):
            Model to use for label detection.
            Supported values: "builtin/stable" (the default
            if unset) and "builtin/latest".
        frame_confidence_threshold (float):
            The confidence threshold we perform filtering on the labels
            from frame-level detection. If not set, it is set to 0.4 by
            default. The valid range for this threshold is [0.1, 0.9].
            Any value set outside of this range will be clipped. Note:
            For best results, follow the default threshold. We will
            update the default threshold everytime when we release a new
            model.
        video_confidence_threshold (float):
            The confidence threshold we perform filtering on the labels
            from video-level and shot-level detections. If not set, it's
            set to 0.3 by default. The valid range for this threshold is
            [0.1, 0.9]. Any value set outside of this range will be
            clipped. Note: For best results, follow the default
            threshold. We will update the default threshold everytime
            when we release a new model.
    """

    label_detection_mode = proto.Field(proto.ENUM, number=1, enum="LabelDetectionMode",)

    stationary_camera = proto.Field(proto.BOOL, number=2)

    model = proto.Field(proto.STRING, number=3)

    frame_confidence_threshold = proto.Field(proto.FLOAT, number=4)

    video_confidence_threshold = proto.Field(proto.FLOAT, number=5)


class ShotChangeDetectionConfig(proto.Message):
    r"""Config for SHOT_CHANGE_DETECTION.

    Attributes:
        model (str):
            Model to use for shot change detection.
            Supported values: "builtin/stable" (the default
            if unset) and "builtin/latest".
    """

    model = proto.Field(proto.STRING, number=1)


class ObjectTrackingConfig(proto.Message):
    r"""Config for OBJECT_TRACKING.

    Attributes:
        model (str):
            Model to use for object tracking.
            Supported values: "builtin/stable" (the default
            if unset) and "builtin/latest".
    """

    model = proto.Field(proto.STRING, number=1)


class ExplicitContentDetectionConfig(proto.Message):
    r"""Config for EXPLICIT_CONTENT_DETECTION.

    Attributes:
        model (str):
            Model to use for explicit content detection.
            Supported values: "builtin/stable" (the default
            if unset) and "builtin/latest".
    """

    model = proto.Field(proto.STRING, number=1)


class FaceDetectionConfig(proto.Message):
    r"""Config for FACE_DETECTION.

    Attributes:
        model (str):
            Model to use for face detection.
            Supported values: "builtin/stable" (the default
            if unset) and "builtin/latest".
        include_bounding_boxes (bool):
            Whether bounding boxes are included in the
            face annotation output.
        include_attributes (bool):
            Whether to enable face attributes detection, such as
            glasses, dark_glasses, mouth_open etc. Ignored if
            'include_bounding_boxes' is set to false.
    """

    model = proto.Field(proto.STRING, number=1)

    include_bounding_boxes = proto.Field(proto.BOOL, number=2)

    include_attributes = proto.Field(proto.BOOL, number=5)


class PersonDetectionConfig(proto.Message):
    r"""Config for PERSON_DETECTION.

    Attributes:
        include_bounding_boxes (bool):
            Whether bounding boxes are included in the
            person detection annotation output.
        include_pose_landmarks (bool):
            Whether to enable pose landmarks detection. Ignored if
            'include_bounding_boxes' is set to false.
        include_attributes (bool):
            Whether to enable person attributes detection, such as cloth
            color (black, blue, etc), type (coat, dress, etc), pattern
            (plain, floral, etc), hair, etc. Ignored if
            'include_bounding_boxes' is set to false.
    """

    include_bounding_boxes = proto.Field(proto.BOOL, number=1)

    include_pose_landmarks = proto.Field(proto.BOOL, number=2)

    include_attributes = proto.Field(proto.BOOL, number=3)


class TextDetectionConfig(proto.Message):
    r"""Config for TEXT_DETECTION.

    Attributes:
        language_hints (Sequence[str]):
            Language hint can be specified if the
            language to be detected is known a priori. It
            can increase the accuracy of the detection.
            Language hint must be language code in BCP-47
            format.

            Automatic language detection is performed if no
            hint is provided.
        model (str):
            Model to use for text detection.
            Supported values: "builtin/stable" (the default
            if unset) and "builtin/latest".
    """

    language_hints = proto.RepeatedField(proto.STRING, number=1)

    model = proto.Field(proto.STRING, number=2)


class VideoSegment(proto.Message):
    r"""Video segment.

    Attributes:
        start_time_offset (~.duration.Duration):
            Time-offset, relative to the beginning of the
            video, corresponding to the start of the segment
            (inclusive).
        end_time_offset (~.duration.Duration):
            Time-offset, relative to the beginning of the
            video, corresponding to the end of the segment
            (inclusive).
    """

    start_time_offset = proto.Field(proto.MESSAGE, number=1, message=duration.Duration,)

    end_time_offset = proto.Field(proto.MESSAGE, number=2, message=duration.Duration,)


class LabelSegment(proto.Message):
    r"""Video segment level annotation results for label detection.

    Attributes:
        segment (~.video_intelligence.VideoSegment):
            Video segment where a label was detected.
        confidence (float):
            Confidence that the label is accurate. Range: [0, 1].
    """

    segment = proto.Field(proto.MESSAGE, number=1, message="VideoSegment",)

    confidence = proto.Field(proto.FLOAT, number=2)


class LabelFrame(proto.Message):
    r"""Video frame level annotation results for label detection.

    Attributes:
        time_offset (~.duration.Duration):
            Time-offset, relative to the beginning of the
            video, corresponding to the video frame for this
            location.
        confidence (float):
            Confidence that the label is accurate. Range: [0, 1].
    """

    time_offset = proto.Field(proto.MESSAGE, number=1, message=duration.Duration,)

    confidence = proto.Field(proto.FLOAT, number=2)


class Entity(proto.Message):
    r"""Detected entity from video analysis.

    Attributes:
        entity_id (str):
            Opaque entity ID. Some IDs may be available in `Google
            Knowledge Graph Search
            API <https://developers.google.com/knowledge-graph/>`__.
        description (str):
            Textual description, e.g., ``Fixed-gear bicycle``.
        language_code (str):
            Language code for ``description`` in BCP-47 format.
    """

    entity_id = proto.Field(proto.STRING, number=1)

    description = proto.Field(proto.STRING, number=2)

    language_code = proto.Field(proto.STRING, number=3)


class LabelAnnotation(proto.Message):
    r"""Label annotation.

    Attributes:
        entity (~.video_intelligence.Entity):
            Detected entity.
        category_entities (Sequence[~.video_intelligence.Entity]):
            Common categories for the detected entity. For example, when
            the label is ``Terrier``, the category is likely ``dog``.
            And in some cases there might be more than one categories
            e.g., ``Terrier`` could also be a ``pet``.
        segments (Sequence[~.video_intelligence.LabelSegment]):
            All video segments where a label was
            detected.
        frames (Sequence[~.video_intelligence.LabelFrame]):
            All video frames where a label was detected.
    """

    entity = proto.Field(proto.MESSAGE, number=1, message="Entity",)

    category_entities = proto.RepeatedField(proto.MESSAGE, number=2, message="Entity",)

    segments = proto.RepeatedField(proto.MESSAGE, number=3, message="LabelSegment",)

    frames = proto.RepeatedField(proto.MESSAGE, number=4, message="LabelFrame",)


class ExplicitContentFrame(proto.Message):
    r"""Video frame level annotation results for explicit content.

    Attributes:
        time_offset (~.duration.Duration):
            Time-offset, relative to the beginning of the
            video, corresponding to the video frame for this
            location.
        pornography_likelihood (~.video_intelligence.Likelihood):
            Likelihood of the pornography content..
    """

    time_offset = proto.Field(proto.MESSAGE, number=1, message=duration.Duration,)

    pornography_likelihood = proto.Field(proto.ENUM, number=2, enum="Likelihood",)


class ExplicitContentAnnotation(proto.Message):
    r"""Explicit content annotation (based on per-frame visual
    signals only). If no explicit content has been detected in a
    frame, no annotations are present for that frame.

    Attributes:
        frames (Sequence[~.video_intelligence.ExplicitContentFrame]):
            All video frames where explicit content was
            detected.
    """

    frames = proto.RepeatedField(
        proto.MESSAGE, number=1, message="ExplicitContentFrame",
    )


class NormalizedBoundingBox(proto.Message):
    r"""Normalized bounding box. The normalized vertex coordinates are
    relative to the original image. Range: [0, 1].

    Attributes:
        left (float):
            Left X coordinate.
        top (float):
            Top Y coordinate.
        right (float):
            Right X coordinate.
        bottom (float):
            Bottom Y coordinate.
    """

    left = proto.Field(proto.FLOAT, number=1)

    top = proto.Field(proto.FLOAT, number=2)

    right = proto.Field(proto.FLOAT, number=3)

    bottom = proto.Field(proto.FLOAT, number=4)


class TimestampedObject(proto.Message):
    r"""For tracking related features. An object at time_offset with
    attributes, and located with normalized_bounding_box.

    Attributes:
        normalized_bounding_box (~.video_intelligence.NormalizedBoundingBox):
            Normalized Bounding box in a frame, where the
            object is located.
        time_offset (~.duration.Duration):
            Time-offset, relative to the beginning of the
            video, corresponding to the video frame for this
            object.
        attributes (Sequence[~.video_intelligence.DetectedAttribute]):
            Optional. The attributes of the object in the
            bounding box.
        landmarks (Sequence[~.video_intelligence.DetectedLandmark]):
            Optional. The detected landmarks.
    """

    normalized_bounding_box = proto.Field(
        proto.MESSAGE, number=1, message="NormalizedBoundingBox",
    )

    time_offset = proto.Field(proto.MESSAGE, number=2, message=duration.Duration,)

    attributes = proto.RepeatedField(
        proto.MESSAGE, number=3, message="DetectedAttribute",
    )

    landmarks = proto.RepeatedField(
        proto.MESSAGE, number=4, message="DetectedLandmark",
    )


class Track(proto.Message):
    r"""A track of an object instance.

    Attributes:
        segment (~.video_intelligence.VideoSegment):
            Video segment of a track.
        timestamped_objects (Sequence[~.video_intelligence.TimestampedObject]):
            The object with timestamp and attributes per
            frame in the track.
        attributes (Sequence[~.video_intelligence.DetectedAttribute]):
            Optional. Attributes in the track level.
        confidence (float):
            Optional. The confidence score of the tracked
            object.
    """

    segment = proto.Field(proto.MESSAGE, number=1, message="VideoSegment",)

    timestamped_objects = proto.RepeatedField(
        proto.MESSAGE, number=2, message="TimestampedObject",
    )

    attributes = proto.RepeatedField(
        proto.MESSAGE, number=3, message="DetectedAttribute",
    )

    confidence = proto.Field(proto.FLOAT, number=4)


class DetectedAttribute(proto.Message):
    r"""A generic detected attribute represented by name in string
    format.

    Attributes:
        name (str):
            The name of the attribute, for example, glasses,
            dark_glasses, mouth_open. A full list of supported type
            names will be provided in the document.
        confidence (float):
            Detected attribute confidence. Range [0, 1].
        value (str):
            Text value of the detection result. For
            example, the value for "HairColor" can be
            "black", "blonde", etc.
    """

    name = proto.Field(proto.STRING, number=1)

    confidence = proto.Field(proto.FLOAT, number=2)

    value = proto.Field(proto.STRING, number=3)


class Celebrity(proto.Message):
    r"""Celebrity definition.

    Attributes:
        name (str):
            The resource name of the celebrity. Have the format
            ``video-intelligence/kg-mid`` indicates a celebrity from
            preloaded gallery. kg-mid is the id in Google knowledge
            graph, which is unique for the celebrity.
        display_name (str):
            The celebrity name.
        description (str):
            Textual description of additional information
            about the celebrity, if applicable.
    """

    name = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    description = proto.Field(proto.STRING, number=3)


class CelebrityTrack(proto.Message):
    r"""The annotation result of a celebrity face track.
    RecognizedCelebrity field could be empty if the face track does
    not have any matched celebrities.

    Attributes:
        celebrities (Sequence[~.video_intelligence.CelebrityTrack.RecognizedCelebrity]):
            Top N match of the celebrities for the face
            in this track.
        face_track (~.video_intelligence.Track):
            A track of a person's face.
    """

    class RecognizedCelebrity(proto.Message):
        r"""The recognized celebrity with confidence score.

        Attributes:
            celebrity (~.video_intelligence.Celebrity):
                The recognized celebrity.
            confidence (float):
                Recognition confidence. Range [0, 1].
        """

        celebrity = proto.Field(proto.MESSAGE, number=1, message="Celebrity",)

        confidence = proto.Field(proto.FLOAT, number=2)

    celebrities = proto.RepeatedField(
        proto.MESSAGE, number=1, message=RecognizedCelebrity,
    )

    face_track = proto.Field(proto.MESSAGE, number=3, message="Track",)


class CelebrityRecognitionAnnotation(proto.Message):
    r"""Celebrity recognition annotation per video.

    Attributes:
        celebrity_tracks (Sequence[~.video_intelligence.CelebrityTrack]):
            The tracks detected from the input video,
            including recognized celebrities and other
            detected faces in the video.
    """

    celebrity_tracks = proto.RepeatedField(
        proto.MESSAGE, number=1, message="CelebrityTrack",
    )


class DetectedLandmark(proto.Message):
    r"""A generic detected landmark represented by name in string
    format and a 2D location.

    Attributes:
        name (str):
            The name of this landmark, for example, left_hand,
            right_shoulder.
        point (~.video_intelligence.NormalizedVertex):
            The 2D point of the detected landmark using
            the normalized image coordindate system. The
            normalized coordinates have the range from 0 to
            1.
        confidence (float):
            The confidence score of the detected landmark. Range [0, 1].
    """

    name = proto.Field(proto.STRING, number=1)

    point = proto.Field(proto.MESSAGE, number=2, message="NormalizedVertex",)

    confidence = proto.Field(proto.FLOAT, number=3)


class FaceDetectionAnnotation(proto.Message):
    r"""Face detection annotation.

    Attributes:
        tracks (Sequence[~.video_intelligence.Track]):
            The face tracks with attributes.
        thumbnail (bytes):
            The thumbnail of a person's face.
    """

    tracks = proto.RepeatedField(proto.MESSAGE, number=3, message="Track",)

    thumbnail = proto.Field(proto.BYTES, number=4)


class PersonDetectionAnnotation(proto.Message):
    r"""Person detection annotation per video.

    Attributes:
        tracks (Sequence[~.video_intelligence.Track]):
            The detected tracks of a person.
    """

    tracks = proto.RepeatedField(proto.MESSAGE, number=1, message="Track",)


class VideoAnnotationResults(proto.Message):
    r"""Annotation results for a single video.

    Attributes:
        input_uri (str):
            Video file location in `Cloud
            Storage <https://cloud.google.com/storage/>`__.
        segment (~.video_intelligence.VideoSegment):
            Video segment on which the annotation is run.
        segment_label_annotations (Sequence[~.video_intelligence.LabelAnnotation]):
            Topical label annotations on video level or
            user-specified segment level. There is exactly
            one element for each unique label.
        segment_presence_label_annotations (Sequence[~.video_intelligence.LabelAnnotation]):
            Presence label annotations on video level or user-specified
            segment level. There is exactly one element for each unique
            label. Compared to the existing topical
            ``segment_label_annotations``, this field presents more
            fine-grained, segment-level labels detected in video content
            and is made available only when the client sets
            ``LabelDetectionConfig.model`` to "builtin/latest" in the
            request.
        shot_label_annotations (Sequence[~.video_intelligence.LabelAnnotation]):
            Topical label annotations on shot level.
            There is exactly one element for each unique
            label.
        shot_presence_label_annotations (Sequence[~.video_intelligence.LabelAnnotation]):
            Presence label annotations on shot level. There is exactly
            one element for each unique label. Compared to the existing
            topical ``shot_label_annotations``, this field presents more
            fine-grained, shot-level labels detected in video content
            and is made available only when the client sets
            ``LabelDetectionConfig.model`` to "builtin/latest" in the
            request.
        frame_label_annotations (Sequence[~.video_intelligence.LabelAnnotation]):
            Label annotations on frame level.
            There is exactly one element for each unique
            label.
        face_detection_annotations (Sequence[~.video_intelligence.FaceDetectionAnnotation]):
            Face detection annotations.
        shot_annotations (Sequence[~.video_intelligence.VideoSegment]):
            Shot annotations. Each shot is represented as
            a video segment.
        explicit_annotation (~.video_intelligence.ExplicitContentAnnotation):
            Explicit content annotation.
        speech_transcriptions (Sequence[~.video_intelligence.SpeechTranscription]):
            Speech transcription.
        text_annotations (Sequence[~.video_intelligence.TextAnnotation]):
            OCR text detection and tracking.
            Annotations for list of detected text snippets.
            Each will have list of frame information
            associated with it.
        object_annotations (Sequence[~.video_intelligence.ObjectTrackingAnnotation]):
            Annotations for list of objects detected and
            tracked in video.
        logo_recognition_annotations (Sequence[~.video_intelligence.LogoRecognitionAnnotation]):
            Annotations for list of logos detected,
            tracked and recognized in video.
        person_detection_annotations (Sequence[~.video_intelligence.PersonDetectionAnnotation]):
            Person detection annotations.
        celebrity_recognition_annotations (~.video_intelligence.CelebrityRecognitionAnnotation):
            Celebrity recognition annotations.
        error (~.status.Status):
            If set, indicates an error. Note that for a single
            ``AnnotateVideoRequest`` some videos may succeed and some
            may fail.
    """

    input_uri = proto.Field(proto.STRING, number=1)

    segment = proto.Field(proto.MESSAGE, number=10, message="VideoSegment",)

    segment_label_annotations = proto.RepeatedField(
        proto.MESSAGE, number=2, message="LabelAnnotation",
    )

    segment_presence_label_annotations = proto.RepeatedField(
        proto.MESSAGE, number=23, message="LabelAnnotation",
    )

    shot_label_annotations = proto.RepeatedField(
        proto.MESSAGE, number=3, message="LabelAnnotation",
    )

    shot_presence_label_annotations = proto.RepeatedField(
        proto.MESSAGE, number=24, message="LabelAnnotation",
    )

    frame_label_annotations = proto.RepeatedField(
        proto.MESSAGE, number=4, message="LabelAnnotation",
    )

    face_detection_annotations = proto.RepeatedField(
        proto.MESSAGE, number=13, message="FaceDetectionAnnotation",
    )

    shot_annotations = proto.RepeatedField(
        proto.MESSAGE, number=6, message="VideoSegment",
    )

    explicit_annotation = proto.Field(
        proto.MESSAGE, number=7, message="ExplicitContentAnnotation",
    )

    speech_transcriptions = proto.RepeatedField(
        proto.MESSAGE, number=11, message="SpeechTranscription",
    )

    text_annotations = proto.RepeatedField(
        proto.MESSAGE, number=12, message="TextAnnotation",
    )

    object_annotations = proto.RepeatedField(
        proto.MESSAGE, number=14, message="ObjectTrackingAnnotation",
    )

    logo_recognition_annotations = proto.RepeatedField(
        proto.MESSAGE, number=19, message="LogoRecognitionAnnotation",
    )

    person_detection_annotations = proto.RepeatedField(
        proto.MESSAGE, number=20, message="PersonDetectionAnnotation",
    )

    celebrity_recognition_annotations = proto.Field(
        proto.MESSAGE, number=21, message="CelebrityRecognitionAnnotation",
    )

    error = proto.Field(proto.MESSAGE, number=9, message=status.Status,)


class AnnotateVideoResponse(proto.Message):
    r"""Video annotation response. Included in the ``response`` field of the
    ``Operation`` returned by the ``GetOperation`` call of the
    ``google::longrunning::Operations`` service.

    Attributes:
        annotation_results (Sequence[~.video_intelligence.VideoAnnotationResults]):
            Annotation results for all videos specified in
            ``AnnotateVideoRequest``.
    """

    annotation_results = proto.RepeatedField(
        proto.MESSAGE, number=1, message="VideoAnnotationResults",
    )


class VideoAnnotationProgress(proto.Message):
    r"""Annotation progress for a single video.

    Attributes:
        input_uri (str):
            Video file location in `Cloud
            Storage <https://cloud.google.com/storage/>`__.
        progress_percent (int):
            Approximate percentage processed thus far.
            Guaranteed to be 100 when fully processed.
        start_time (~.timestamp.Timestamp):
            Time when the request was received.
        update_time (~.timestamp.Timestamp):
            Time of the most recent update.
        feature (~.video_intelligence.Feature):
            Specifies which feature is being tracked if
            the request contains more than one feature.
        segment (~.video_intelligence.VideoSegment):
            Specifies which segment is being tracked if
            the request contains more than one segment.
    """

    input_uri = proto.Field(proto.STRING, number=1)

    progress_percent = proto.Field(proto.INT32, number=2)

    start_time = proto.Field(proto.MESSAGE, number=3, message=timestamp.Timestamp,)

    update_time = proto.Field(proto.MESSAGE, number=4, message=timestamp.Timestamp,)

    feature = proto.Field(proto.ENUM, number=5, enum="Feature",)

    segment = proto.Field(proto.MESSAGE, number=6, message="VideoSegment",)


class AnnotateVideoProgress(proto.Message):
    r"""Video annotation progress. Included in the ``metadata`` field of the
    ``Operation`` returned by the ``GetOperation`` call of the
    ``google::longrunning::Operations`` service.

    Attributes:
        annotation_progress (Sequence[~.video_intelligence.VideoAnnotationProgress]):
            Progress metadata for all videos specified in
            ``AnnotateVideoRequest``.
    """

    annotation_progress = proto.RepeatedField(
        proto.MESSAGE, number=1, message="VideoAnnotationProgress",
    )


class SpeechTranscriptionConfig(proto.Message):
    r"""Config for SPEECH_TRANSCRIPTION.

    Attributes:
        language_code (str):
            Required. *Required* The language of the supplied audio as a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag. Example: "en-US". See `Language
            Support <https://cloud.google.com/speech/docs/languages>`__
            for a list of the currently supported language codes.
        max_alternatives (int):
            Optional. Maximum number of recognition hypotheses to be
            returned. Specifically, the maximum number of
            ``SpeechRecognitionAlternative`` messages within each
            ``SpeechTranscription``. The server may return fewer than
            ``max_alternatives``. Valid values are ``0``-``30``. A value
            of ``0`` or ``1`` will return a maximum of one. If omitted,
            will return a maximum of one.
        filter_profanity (bool):
            Optional. If set to ``true``, the server will attempt to
            filter out profanities, replacing all but the initial
            character in each filtered word with asterisks, e.g. "f***".
            If set to ``false`` or omitted, profanities won't be
            filtered out.
        speech_contexts (Sequence[~.video_intelligence.SpeechContext]):
            Optional. A means to provide context to
            assist the speech recognition.
        enable_automatic_punctuation (bool):
            Optional. If 'true', adds punctuation to
            recognition result hypotheses. This feature is
            only available in select languages. Setting this
            for requests in other languages has no effect at
            all. The default 'false' value does not add
            punctuation to result hypotheses. NOTE: "This is
            currently offered as an experimental service,
            complimentary to all users. In the future this
            may be exclusively available as a premium
            feature.".
        audio_tracks (Sequence[int]):
            Optional. For file formats, such as MXF or
            MKV, supporting multiple audio tracks, specify
            up to two tracks. Default: track 0.
        enable_speaker_diarization (bool):
            Optional. If 'true', enables speaker detection for each
            recognized word in the top alternative of the recognition
            result using a speaker_tag provided in the WordInfo. Note:
            When this is true, we send all the words from the beginning
            of the audio for the top alternative in every consecutive
            response. This is done in order to improve our speaker tags
            as our models learn to identify the speakers in the
            conversation over time.
        diarization_speaker_count (int):
            Optional. If set, specifies the estimated number of speakers
            in the conversation. If not set, defaults to '2'. Ignored
            unless enable_speaker_diarization is set to true.
        enable_word_confidence (bool):
            Optional. If ``true``, the top result includes a list of
            words and the confidence for those words. If ``false``, no
            word-level confidence information is returned. The default
            is ``false``.
    """

    language_code = proto.Field(proto.STRING, number=1)

    max_alternatives = proto.Field(proto.INT32, number=2)

    filter_profanity = proto.Field(proto.BOOL, number=3)

    speech_contexts = proto.RepeatedField(
        proto.MESSAGE, number=4, message="SpeechContext",
    )

    enable_automatic_punctuation = proto.Field(proto.BOOL, number=5)

    audio_tracks = proto.RepeatedField(proto.INT32, number=6)

    enable_speaker_diarization = proto.Field(proto.BOOL, number=7)

    diarization_speaker_count = proto.Field(proto.INT32, number=8)

    enable_word_confidence = proto.Field(proto.BOOL, number=9)


class SpeechContext(proto.Message):
    r"""Provides "hints" to the speech recognizer to favor specific
    words and phrases in the results.

    Attributes:
        phrases (Sequence[str]):
            Optional. A list of strings containing words and phrases
            "hints" so that the speech recognition is more likely to
            recognize them. This can be used to improve the accuracy for
            specific words and phrases, for example, if specific
            commands are typically spoken by the user. This can also be
            used to add additional words to the vocabulary of the
            recognizer. See `usage
            limits <https://cloud.google.com/speech/limits#content>`__.
    """

    phrases = proto.RepeatedField(proto.STRING, number=1)


class SpeechTranscription(proto.Message):
    r"""A speech recognition result corresponding to a portion of the
    audio.

    Attributes:
        alternatives (Sequence[~.video_intelligence.SpeechRecognitionAlternative]):
            May contain one or more recognition hypotheses (up to the
            maximum specified in ``max_alternatives``). These
            alternatives are ordered in terms of accuracy, with the top
            (first) alternative being the most probable, as ranked by
            the recognizer.
        language_code (str):
            Output only. The
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag of the language in this result. This language
            code was detected to have the most likelihood of being
            spoken in the audio.
    """

    alternatives = proto.RepeatedField(
        proto.MESSAGE, number=1, message="SpeechRecognitionAlternative",
    )

    language_code = proto.Field(proto.STRING, number=2)


class SpeechRecognitionAlternative(proto.Message):
    r"""Alternative hypotheses (a.k.a. n-best list).

    Attributes:
        transcript (str):
            Transcript text representing the words that
            the user spoke.
        confidence (float):
            Output only. The confidence estimate between 0.0 and 1.0. A
            higher number indicates an estimated greater likelihood that
            the recognized words are correct. This field is set only for
            the top alternative. This field is not guaranteed to be
            accurate and users should not rely on it to be always
            provided. The default of 0.0 is a sentinel value indicating
            ``confidence`` was not set.
        words (Sequence[~.video_intelligence.WordInfo]):
            Output only. A list of word-specific information for each
            recognized word. Note: When ``enable_speaker_diarization``
            is set to true, you will see all the words from the
            beginning of the audio.
    """

    transcript = proto.Field(proto.STRING, number=1)

    confidence = proto.Field(proto.FLOAT, number=2)

    words = proto.RepeatedField(proto.MESSAGE, number=3, message="WordInfo",)


class WordInfo(proto.Message):
    r"""Word-specific information for recognized words. Word information is
    only included in the response when certain request parameters are
    set, such as ``enable_word_time_offsets``.

    Attributes:
        start_time (~.duration.Duration):
            Time offset relative to the beginning of the audio, and
            corresponding to the start of the spoken word. This field is
            only set if ``enable_word_time_offsets=true`` and only in
            the top hypothesis. This is an experimental feature and the
            accuracy of the time offset can vary.
        end_time (~.duration.Duration):
            Time offset relative to the beginning of the audio, and
            corresponding to the end of the spoken word. This field is
            only set if ``enable_word_time_offsets=true`` and only in
            the top hypothesis. This is an experimental feature and the
            accuracy of the time offset can vary.
        word (str):
            The word corresponding to this set of
            information.
        confidence (float):
            Output only. The confidence estimate between 0.0 and 1.0. A
            higher number indicates an estimated greater likelihood that
            the recognized words are correct. This field is set only for
            the top alternative. This field is not guaranteed to be
            accurate and users should not rely on it to be always
            provided. The default of 0.0 is a sentinel value indicating
            ``confidence`` was not set.
        speaker_tag (int):
            Output only. A distinct integer value is assigned for every
            speaker within the audio. This field specifies which one of
            those speakers was detected to have spoken this word. Value
            ranges from 1 up to diarization_speaker_count, and is only
            set if speaker diarization is enabled.
    """

    start_time = proto.Field(proto.MESSAGE, number=1, message=duration.Duration,)

    end_time = proto.Field(proto.MESSAGE, number=2, message=duration.Duration,)

    word = proto.Field(proto.STRING, number=3)

    confidence = proto.Field(proto.FLOAT, number=4)

    speaker_tag = proto.Field(proto.INT32, number=5)


class NormalizedVertex(proto.Message):
    r"""A vertex represents a 2D point in the image.
    NOTE: the normalized vertex coordinates are relative to the
    original image and range from 0 to 1.

    Attributes:
        x (float):
            X coordinate.
        y (float):
            Y coordinate.
    """

    x = proto.Field(proto.FLOAT, number=1)

    y = proto.Field(proto.FLOAT, number=2)


class NormalizedBoundingPoly(proto.Message):
    r"""Normalized bounding polygon for text (that might not be aligned with
    axis). Contains list of the corner points in clockwise order
    starting from top-left corner. For example, for a rectangular
    bounding box: When the text is horizontal it might look like: 0----1
    \| \| 3----2

    When it's clockwise rotated 180 degrees around the top-left corner
    it becomes: 2----3 \| \| 1----0

    and the vertex order will still be (0, 1, 2, 3). Note that values
    can be less than 0, or greater than 1 due to trignometric
    calculations for location of the box.

    Attributes:
        vertices (Sequence[~.video_intelligence.NormalizedVertex]):
            Normalized vertices of the bounding polygon.
    """

    vertices = proto.RepeatedField(proto.MESSAGE, number=1, message="NormalizedVertex",)


class TextSegment(proto.Message):
    r"""Video segment level annotation results for text detection.

    Attributes:
        segment (~.video_intelligence.VideoSegment):
            Video segment where a text snippet was
            detected.
        confidence (float):
            Confidence for the track of detected text. It
            is calculated as the highest over all frames
            where OCR detected text appears.
        frames (Sequence[~.video_intelligence.TextFrame]):
            Information related to the frames where OCR
            detected text appears.
    """

    segment = proto.Field(proto.MESSAGE, number=1, message="VideoSegment",)

    confidence = proto.Field(proto.FLOAT, number=2)

    frames = proto.RepeatedField(proto.MESSAGE, number=3, message="TextFrame",)


class TextFrame(proto.Message):
    r"""Video frame level annotation results for text annotation
    (OCR). Contains information regarding timestamp and bounding box
    locations for the frames containing detected OCR text snippets.

    Attributes:
        rotated_bounding_box (~.video_intelligence.NormalizedBoundingPoly):
            Bounding polygon of the detected text for
            this frame.
        time_offset (~.duration.Duration):
            Timestamp of this frame.
    """

    rotated_bounding_box = proto.Field(
        proto.MESSAGE, number=1, message="NormalizedBoundingPoly",
    )

    time_offset = proto.Field(proto.MESSAGE, number=2, message=duration.Duration,)


class TextAnnotation(proto.Message):
    r"""Annotations related to one detected OCR text snippet. This
    will contain the corresponding text, confidence value, and frame
    level information for each detection.

    Attributes:
        text (str):
            The detected text.
        segments (Sequence[~.video_intelligence.TextSegment]):
            All video segments where OCR detected text
            appears.
    """

    text = proto.Field(proto.STRING, number=1)

    segments = proto.RepeatedField(proto.MESSAGE, number=2, message="TextSegment",)


class ObjectTrackingFrame(proto.Message):
    r"""Video frame level annotations for object detection and
    tracking. This field stores per frame location, time offset, and
    confidence.

    Attributes:
        normalized_bounding_box (~.video_intelligence.NormalizedBoundingBox):
            The normalized bounding box location of this
            object track for the frame.
        time_offset (~.duration.Duration):
            The timestamp of the frame in microseconds.
    """

    normalized_bounding_box = proto.Field(
        proto.MESSAGE, number=1, message="NormalizedBoundingBox",
    )

    time_offset = proto.Field(proto.MESSAGE, number=2, message=duration.Duration,)


class ObjectTrackingAnnotation(proto.Message):
    r"""Annotations corresponding to one tracked object.

    Attributes:
        segment (~.video_intelligence.VideoSegment):
            Non-streaming batch mode ONLY.
            Each object track corresponds to one video
            segment where it appears.
        track_id (int):
            Streaming mode ONLY. In streaming mode, we do not know the
            end time of a tracked object before it is completed. Hence,
            there is no VideoSegment info returned. Instead, we provide
            a unique identifiable integer track_id so that the customers
            can correlate the results of the ongoing
            ObjectTrackAnnotation of the same track_id over time.
        entity (~.video_intelligence.Entity):
            Entity to specify the object category that
            this track is labeled as.
        confidence (float):
            Object category's labeling confidence of this
            track.
        frames (Sequence[~.video_intelligence.ObjectTrackingFrame]):
            Information corresponding to all frames where
            this object track appears. Non-streaming batch
            mode: it may be one or multiple
            ObjectTrackingFrame messages in frames.
            Streaming mode: it can only be one
            ObjectTrackingFrame message in frames.
    """

    segment = proto.Field(
        proto.MESSAGE, number=3, oneof="track_info", message="VideoSegment",
    )

    track_id = proto.Field(proto.INT64, number=5, oneof="track_info")

    entity = proto.Field(proto.MESSAGE, number=1, message="Entity",)

    confidence = proto.Field(proto.FLOAT, number=4)

    frames = proto.RepeatedField(
        proto.MESSAGE, number=2, message="ObjectTrackingFrame",
    )


class LogoRecognitionAnnotation(proto.Message):
    r"""Annotation corresponding to one detected, tracked and
    recognized logo class.

    Attributes:
        entity (~.video_intelligence.Entity):
            Entity category information to specify the
            logo class that all the logo tracks within this
            LogoRecognitionAnnotation are recognized as.
        tracks (Sequence[~.video_intelligence.Track]):
            All logo tracks where the recognized logo
            appears. Each track corresponds to one logo
            instance appearing in consecutive frames.
        segments (Sequence[~.video_intelligence.VideoSegment]):
            All video segments where the recognized logo
            appears. There might be multiple instances of
            the same logo class appearing in one
            VideoSegment.
    """

    entity = proto.Field(proto.MESSAGE, number=1, message="Entity",)

    tracks = proto.RepeatedField(proto.MESSAGE, number=2, message="Track",)

    segments = proto.RepeatedField(proto.MESSAGE, number=3, message="VideoSegment",)


class StreamingAnnotateVideoRequest(proto.Message):
    r"""The top-level message sent by the client for the
    ``StreamingAnnotateVideo`` method. Multiple
    ``StreamingAnnotateVideoRequest`` messages are sent. The first
    message must only contain a ``StreamingVideoConfig`` message. All
    subsequent messages must only contain ``input_content`` data.

    Attributes:
        video_config (~.video_intelligence.StreamingVideoConfig):
            Provides information to the annotator, specifing how to
            process the request. The first
            ``AnnotateStreamingVideoRequest`` message must only contain
            a ``video_config`` message.
        input_content (bytes):
            The video data to be annotated. Chunks of video data are
            sequentially sent in ``StreamingAnnotateVideoRequest``
            messages. Except the initial
            ``StreamingAnnotateVideoRequest`` message containing only
            ``video_config``, all subsequent
            ``AnnotateStreamingVideoRequest`` messages must only contain
            ``input_content`` field. Note: as with all bytes fields,
            protobuffers use a pure binary representation (not base64).
    """

    video_config = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="streaming_request",
        message="StreamingVideoConfig",
    )

    input_content = proto.Field(proto.BYTES, number=2, oneof="streaming_request")


class StreamingVideoConfig(proto.Message):
    r"""Provides information to the annotator that specifies how to
    process the request.

    Attributes:
        shot_change_detection_config (~.video_intelligence.StreamingShotChangeDetectionConfig):
            Config for STREAMING_SHOT_CHANGE_DETECTION.
        label_detection_config (~.video_intelligence.StreamingLabelDetectionConfig):
            Config for STREAMING_LABEL_DETECTION.
        explicit_content_detection_config (~.video_intelligence.StreamingExplicitContentDetectionConfig):
            Config for STREAMING_EXPLICIT_CONTENT_DETECTION.
        object_tracking_config (~.video_intelligence.StreamingObjectTrackingConfig):
            Config for STREAMING_OBJECT_TRACKING.
        automl_action_recognition_config (~.video_intelligence.StreamingAutomlActionRecognitionConfig):
            Config for STREAMING_AUTOML_ACTION_RECOGNITION.
        automl_classification_config (~.video_intelligence.StreamingAutomlClassificationConfig):
            Config for STREAMING_AUTOML_CLASSIFICATION.
        automl_object_tracking_config (~.video_intelligence.StreamingAutomlObjectTrackingConfig):
            Config for STREAMING_AUTOML_OBJECT_TRACKING.
        feature (~.video_intelligence.StreamingFeature):
            Requested annotation feature.
        storage_config (~.video_intelligence.StreamingStorageConfig):
            Streaming storage option. By default: storage
            is disabled.
    """

    shot_change_detection_config = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="streaming_config",
        message="StreamingShotChangeDetectionConfig",
    )

    label_detection_config = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="streaming_config",
        message="StreamingLabelDetectionConfig",
    )

    explicit_content_detection_config = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="streaming_config",
        message="StreamingExplicitContentDetectionConfig",
    )

    object_tracking_config = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="streaming_config",
        message="StreamingObjectTrackingConfig",
    )

    automl_action_recognition_config = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="streaming_config",
        message="StreamingAutomlActionRecognitionConfig",
    )

    automl_classification_config = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="streaming_config",
        message="StreamingAutomlClassificationConfig",
    )

    automl_object_tracking_config = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="streaming_config",
        message="StreamingAutomlObjectTrackingConfig",
    )

    feature = proto.Field(proto.ENUM, number=1, enum="StreamingFeature",)

    storage_config = proto.Field(
        proto.MESSAGE, number=30, message="StreamingStorageConfig",
    )


class StreamingAnnotateVideoResponse(proto.Message):
    r"""``StreamingAnnotateVideoResponse`` is the only message returned to
    the client by ``StreamingAnnotateVideo``. A series of zero or more
    ``StreamingAnnotateVideoResponse`` messages are streamed back to the
    client.

    Attributes:
        error (~.status.Status):
            If set, returns a [google.rpc.Status][google.rpc.Status]
            message that specifies the error for the operation.
        annotation_results (~.video_intelligence.StreamingVideoAnnotationResults):
            Streaming annotation results.
        annotation_results_uri (str):
            Google Cloud Storage(GCS) URI that stores annotation results
            of one streaming session in JSON format. It is the
            annotation_result_storage_directory from the request
            followed by '/cloud_project_number-session_id'.
    """

    error = proto.Field(proto.MESSAGE, number=1, message=status.Status,)

    annotation_results = proto.Field(
        proto.MESSAGE, number=2, message="StreamingVideoAnnotationResults",
    )

    annotation_results_uri = proto.Field(proto.STRING, number=3)


class StreamingVideoAnnotationResults(proto.Message):
    r"""Streaming annotation results corresponding to a portion of
    the video that is currently being processed.

    Attributes:
        shot_annotations (Sequence[~.video_intelligence.VideoSegment]):
            Shot annotation results. Each shot is
            represented as a video segment.
        label_annotations (Sequence[~.video_intelligence.LabelAnnotation]):
            Label annotation results.
        explicit_annotation (~.video_intelligence.ExplicitContentAnnotation):
            Explicit content annotation results.
        object_annotations (Sequence[~.video_intelligence.ObjectTrackingAnnotation]):
            Object tracking results.
    """

    shot_annotations = proto.RepeatedField(
        proto.MESSAGE, number=1, message="VideoSegment",
    )

    label_annotations = proto.RepeatedField(
        proto.MESSAGE, number=2, message="LabelAnnotation",
    )

    explicit_annotation = proto.Field(
        proto.MESSAGE, number=3, message="ExplicitContentAnnotation",
    )

    object_annotations = proto.RepeatedField(
        proto.MESSAGE, number=4, message="ObjectTrackingAnnotation",
    )


class StreamingShotChangeDetectionConfig(proto.Message):
    r"""Config for STREAMING_SHOT_CHANGE_DETECTION."""


class StreamingLabelDetectionConfig(proto.Message):
    r"""Config for STREAMING_LABEL_DETECTION.

    Attributes:
        stationary_camera (bool):
            Whether the video has been captured from a
            stationary (i.e. non-moving) camera. When set to
            true, might improve detection accuracy for
            moving objects. Default: false.
    """

    stationary_camera = proto.Field(proto.BOOL, number=1)


class StreamingExplicitContentDetectionConfig(proto.Message):
    r"""Config for STREAMING_EXPLICIT_CONTENT_DETECTION."""


class StreamingObjectTrackingConfig(proto.Message):
    r"""Config for STREAMING_OBJECT_TRACKING."""


class StreamingAutomlActionRecognitionConfig(proto.Message):
    r"""Config for STREAMING_AUTOML_ACTION_RECOGNITION.

    Attributes:
        model_name (str):
            Resource name of AutoML model. Format:
            ``projects/{project_id}/locations/{location_id}/models/{model_id}``
    """

    model_name = proto.Field(proto.STRING, number=1)


class StreamingAutomlClassificationConfig(proto.Message):
    r"""Config for STREAMING_AUTOML_CLASSIFICATION.

    Attributes:
        model_name (str):
            Resource name of AutoML model. Format:
            ``projects/{project_number}/locations/{location_id}/models/{model_id}``
    """

    model_name = proto.Field(proto.STRING, number=1)


class StreamingAutomlObjectTrackingConfig(proto.Message):
    r"""Config for STREAMING_AUTOML_OBJECT_TRACKING.

    Attributes:
        model_name (str):
            Resource name of AutoML model. Format:
            ``projects/{project_id}/locations/{location_id}/models/{model_id}``
    """

    model_name = proto.Field(proto.STRING, number=1)


class StreamingStorageConfig(proto.Message):
    r"""Config for streaming storage option.

    Attributes:
        enable_storage_annotation_result (bool):
            Enable streaming storage. Default: false.
        annotation_result_storage_directory (str):
            Cloud Storage URI to store all annotation results for one
            client. Client should specify this field as the top-level
            storage directory. Annotation results of different sessions
            will be put into different sub-directories denoted by
            project_name and session_id. All sub-directories will be
            auto generated by program and will be made accessible to
            client in response proto. URIs must be specified in the
            following format: ``gs://bucket-id/object-id`` ``bucket-id``
            should be a valid Cloud Storage bucket created by client and
            bucket permission shall also be configured properly.
            ``object-id`` can be arbitrary string that make sense to
            client. Other URI formats will return error and cause Cloud
            Storage write failure.
    """

    enable_storage_annotation_result = proto.Field(proto.BOOL, number=1)

    annotation_result_storage_directory = proto.Field(proto.STRING, number=3)


__all__ = tuple(sorted(__protobuf__.manifest))
