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

import random

from .generate_japanese_alias_from_rng import generate_japanese_alias_from_rng


def generate_japanese_alias(str_or_rng=None):
  if str_or_rng is None:
    rng = random.Random()
    return generate_japanese_alias_from_rng(rng)
  elif isinstance(str_or_rng, str):
    str_ = str_or_rng
    return generate_japanese_alias_from_str(str_)
  else:  # isinstance(str_or_rng, random.Random)
    rng = str_or_rng
    return generate_japanese_alias_from_rng(rng)


def generate_japanese_alias_from_str(str):
  rng = random.Random(str)

  return generate_japanese_alias_from_rng(rng)
