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



def generate_japanese_alias_from_rng(language, rng):
  if language == 'ja':
    from ._ndata import ndata_ja as ndata
    aux = ['の', '・オブ・', '・', 'ザ・']
  elif language == 'zh':
    from ._ndata import ndata_zh as ndata
    aux = ['之', '于', '', '']
  elif language == 'en':
    from ._ndata import ndata_en as ndata
    aux = [' ', ' of ', ' ', 'The ']

  columns_length = len(ndata)

  # See: http://elona.wikiwiki.jp/?%3A%B2%F2%C0%CF%2F%A5%A2%A5%A4%A5%C6%A5%E0#w25458e3
  while True:
    # ja: 1. 先頭文字決定
    while True:
      head_column_index = rng.randrange(columns_length)
      rows_length = len(ndata[head_column_index])
      head_row_index = rng.randrange(rows_length - 1)
      alias = ndata[head_column_index][head_row_index]
      if alias != '':
        break

    # ja: 2. 接続詞の追加判定
    if head_row_index in (0, 1):
      if 1 == rng.randint(1, 10):
        head_row_index = 10
        alias = ndata[head_column_index][head_row_index]
      else:
        alias = alias + aux[0]
    elif head_row_index in (10, 11):
      r25 = rng.randint(1, 25)
      if 1 <= r25 <= 5:
        head_row_index = 0
        alias = ndata[head_column_index][head_row_index]

        # RV letla@github: Workaround for the empty alias
        if alias == '':
          continue

        if 1 == rng.randint(1, 2):
          alias = alias + aux[0]
      elif 6 <= r25 <= 9:
        alias = alias + aux[1]
      elif 10 <= r25 <= 13:
        alias = alias + aux[2]
      elif 14 <= r25 <= 17:
        return aux[3] + alias

    # ja: 3. 末尾文字決定
    for _ in range(100):
      tail_column_index = rng.randrange(columns_length)
      if tail_column_index == head_column_index:
        continue

      head_alias_category = ndata[head_column_index][-1]
      tail_alias_category = ndata[tail_column_index][-1]
      if (head_alias_category == tail_alias_category and
          head_alias_category != '万能'):
        continue

      if head_row_index < 10:
        tail_row_index = rng.randrange(2)
      else:
        tail_row_index = 10 + rng.randrange(2)

      tail_alias = ndata[tail_column_index][tail_row_index]
      if tail_alias == '':
        continue
      else:
        alias = alias + tail_alias
        break
    else:
      continue

    # ja: 4. エラー判定
    if 14 <= len(alias):
      continue

    return alias
