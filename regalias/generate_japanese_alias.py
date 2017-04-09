# Copyright 2017 Letla Fox
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

from random import Random

from .generate_japanese_alias_from_rng import generate_japanese_alias_from_rng
from .generate_japanese_alias_from_str import generate_japanese_alias_from_str


def generate_japanese_alias(language, str_or_rng=None):
  if str_or_rng is None:
    rng = Random()
    return generate_japanese_alias_from_rng(language, rng)
  elif isinstance(str_or_rng, str):
    str_ = str_or_rng
    return generate_japanese_alias_from_str(language, str_)
  else:  # isinstance(str_or_rng, Random)
    rng = str_or_rng
    return generate_japanese_alias_from_rng(language, rng)
