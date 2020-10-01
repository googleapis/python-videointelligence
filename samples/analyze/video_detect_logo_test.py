# Copyright 2020 Google
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

import os

import pytest

import video_detect_logo

RESOURCES = os.path.join(os.path.dirname(__file__), "resources")


# Flaky Bad Gateway
@pytest.mark.flaky(max_runs=3, min_passes=1)
def test_detect_logo(capsys):
    local_file_path = os.path.join(RESOURCES, "googlework_tiny.mp4")

    video_detect_logo.detect_logo(local_file_path=local_file_path)

    out, _ = capsys.readouterr()

    assert "Description" in out
    assert "Confidence" in out
    assert "Start Time Offset" in out
    assert "End Time Offset" in out
