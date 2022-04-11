# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for AnnotateVideo
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-videointelligence


# [START videointelligence_v1p3beta1_generated_VideoIntelligenceService_AnnotateVideo_sync]
from google.cloud import videointelligence_v1p3beta1


def sample_annotate_video():
    # Create a client
    client = videointelligence_v1p3beta1.VideoIntelligenceServiceClient()

    # Initialize request argument(s)
    request = videointelligence_v1p3beta1.AnnotateVideoRequest(
        features="PERSON_DETECTION",
    )

    # Make the request
    operation = client.annotate_video(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END videointelligence_v1p3beta1_generated_VideoIntelligenceService_AnnotateVideo_sync]