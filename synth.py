# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""
import logging

import synthtool as s

from synthtool import gcp
from synthtool.languages import python

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()
versions = ["v1beta2", "v1p1beta1", "v1p2beta1", "v1p3beta1", "v1"]

# ----------------------------------------------------------------------------
# Generate videointelligence GAPIC layer
# ----------------------------------------------------------------------------
for version in versions:
    library = gapic.py_library(
        service="videointelligence",
        version=version,
        bazel_target=f"//google/cloud/videointelligence/{version}:videointelligence-{version}-py",
        include_protos=True,
    )

    s.move(
        library,
        excludes=[
            "setup.py",
            "README.rst",
            "docs/index.rst",
        ],
    )
    s.replace(
        f"google/cloud/videointelligence_{version}/gapic/"
        f"*video_intelligence_service_client.py",
        "google-cloud-video-intelligence",
        "google-cloud-videointelligence",
    )

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(cov_level=70, samples=True, microgenerator=True)

# microgenerator has a good .coveragerc file
s.move(templated_files, excludes=[".coveragerc"])

# ----------------------------------------------------------------------------
# Samples templates
# ----------------------------------------------------------------------------
python.py_samples()

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
