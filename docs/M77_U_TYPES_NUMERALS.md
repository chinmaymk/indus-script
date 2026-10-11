# Primary object types for M328 references 4400–4999

All **142 selected catalogue references** were located and their object codes visually verified in Mahadevan's primary Texts metadata: **97 miniature tablets (code 3) and 45 sealings (code 2)**. No selected object type remains unverified. These are catalogue categories, not inferred numerical meanings or independently re-established materials.

Selection used unique references in `data/processed/m77_u_recovered_lines.jsonl` satisfying 4400 <= reference < 5000. It did not use candidate object codes or treat the whole reference interval as one object category. The actual source pages were PDF 121–139 / printed 110–128; 4704 and 4718 occur on PDF 139, beyond the initial expected page range.

The codebook at printed 30 / PDF 41 identifies numerical column 5 of Texts as the object code. It is the first digit after the four-digit reference. The [ledger](../data/processed/m77_u_types_numerals.json) retains the full six-digit first metadata string, exact reference, PDF and printed page, first side and line codes, verification status and image SHA256 for each selected row. Only layout spacing is collapsed; leading and internal zeros remain intact.

| PDF / printed page | Selected references visually read |
|---|---|
| 121 / 110 | 4401 |
| 122 / 111 | 4402, 4403, 4404, 4405, 4406, 4407, 4410 |
| 123 / 112 | 4419, 4420, 4428 |
| 124 / 113 | 4444, 4445, 4446, 4448 |
| 125 / 114 | 4451, 4452, 4455, 4456, 4457, 4458, 4459, 4461, 4462, 4463 |
| 126 / 115 | 4468, 4469, 4470, 4473, 4475, 4476, 4477, 4479, 4483 |
| 127 / 116 | 4484, 4485, 4487, 4489, 4490, 4491, 4492, 4493, 4494, 4497, 4498, 4499, 4501 |
| 128 / 117 | 4502, 4503, 4504, 4508, 4509, 4510, 4511, 4512, 4515, 4516 |
| 129 / 118 | 4519, 4520, 4522, 4523, 4525, 4528 |
| 130 / 119 | 4543, 4544, 4546, 4548, 4549, 4550, 4551, 4552, 4553, 4554, 4555, 4556 |
| 131 / 120 | 4559, 4562, 4564, 4566, 4571, 4574, 4575 |
| 132 / 121 | 4576, 4577, 4579, 4580, 4581, 4582, 4585, 4586 |
| 133 / 122 | 4587, 4588, 4589, 4591, 4593, 4594, 4595, 4596, 4597 |
| 134 / 123 | 4601, 4602, 4603, 4604, 4605, 4606, 4607, 4610, 4613 |
| 135 / 124 | 4639, 4641, 4642, 4645, 4646, 4647 |
| 136 / 125 | 4649, 4653, 4660, 4661, 4665 |
| 137 / 126 | 4666, 4667, 4670, 4671, 4672, 4673, 4674, 4675, 4678, 4679, 4680, 4681, 4682 |
| 138 / 127 | 4683, 4684, 4686, 4689, 4691, 4692, 4700, 4702 |
| 139 / 128 | 4704, 4718 |

All selected first metadata lines have side 1, line 0. This does not locate their recovered U-bearing line or determine every line's direction. For example, 4660 first prints 210009 on its loss-only first side, while its U-bearing second side prints 20002. Reference 4671 likewise has first metadata 210009 and second-side metadata 20001.

The ledger also preserves changes that a range-based classification would miss: 4594 is explicitly a sealing; 4700 and 4718 are explicitly miniature tablets despite nearby other object types. Every selected row was read rather than filled from surrounding entries.

Whole-page evidence images are retained as `results/primary_pages/m77-u-types-numerals-121.jpg` through 139.jpg, all derived locally from the existing PDF. No downloads occurred. This audit authenticates the primary catalogue's object labels; it does not establish artifact independence, manufacture, capacity or the function of M328.
