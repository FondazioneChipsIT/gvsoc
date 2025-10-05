#
# Copyright (C) 2025 ETH Zurich and University of Bologna
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

# Author: Chi Zhang <chizhang@ethz.ch>

class RMSNorm:

    def __init__(self):

        #Attention parameters
        self.dtype                   = 'fp16'
        self.m_size                  = 512
        self.n_size                  = 512

        #HyperParameters
        ## [Numer]: Whether to check numerical correctness
        self.norm_numer              = 1
        self.norm_numer_chunk        = 8192
