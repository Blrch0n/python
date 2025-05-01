text = """The court heard how Mr. Patterson spoke to his father the morning after the lunch and discovered both his parents had been up since midnight with vomiting and diarrhoea, and that they had called an ambulance.

After trying to call his aunt and uncle, Heather and Ian Wilkinson, he went to their home when they did not answer.

"Ian answered the door. He looked grey and spooked," Mr. Patterson recalled. "Yeah, he was struggling.

"I said, 'How are you?' He said, 'Not good.'"

Mr. Patterson then saw Heather Wilkinson sitting on the couch, he told the court.

"She looked pretty crook. She had a container as a spew bucket," he said.

After Mr. Wilkinson left the room, Heather spoke to him, he confirmed, under questioning from prosecutor Dr. Rogers.

"We didn't have much conversation, but she was puzzled and she said, 'I noticed Erin served herself her food on a coloured plate which was different to the rest.'"

"I acknowledged I'd heard her, but did not progress it as a conversation," he added.

Because he had been told an ambulance would have taken an hour to arrive, Mr. Patterson drove the couple to hospital in the Wilkinsons' car when Heather Wilkinson raised the subject once more.

"She mentioned the coloured plate again. She asked me, 'Is Erin short of crockery? Is that why she would have this different coloured plate that she served herself with?'" Mr. Patterson said.

"I can't remember the exact phrase, but it was something like that."

"And what did you reply?" the prosecutor asked.

"I said yes, Erin doesn't have that many plates and that may be the reason."

Mr. Patterson became emotional again, describing going to see his parents at Korumburra Hospital, where they were in the same room but separate beds.

"Dad was substantially worse than Mum. He was really struggling," he said, fighting back tears.

"He was lying on his side. He was hunched quite noticeably, with a really discoloured face, struggling to speak.

"Speaking was an effort, taking the energy to speak was an effort, and his voice was strained in a way that he wasn't right inside. He was in pain."
"""
d = {}
dw = {}
wrd=text.split()

for ch in wrd:
    if ch in dw:
        dw[ch] += 1
    else:
        dw[ch] = 1
print(dw)

for paragraph in text:
    for ch in paragraph:
        if ch.isalpha():
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

for k in sorted(d.keys()):
    print(f"{k} үсэг {d[k]} ширхэг байна")
print(f'-------------------------------------')
ks = d.keys()
best_key_so_far = list(ks)[0]
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k
print(best_key_so_far + " үсэг хамгийн их буюу " + str(d[best_key_so_far]) + " ширхэг байна")

for k in ks:
    if d[k] < d[best_key_so_far]:
        best_key_so_far = k
print(best_key_so_far + " үсэг хамгийн бага буюу " + str(d[best_key_so_far]) + " ширхэг байна")

word_dict = {}
word = ""
total_words = 0
for paragraph in text:
    for ch in paragraph:
        if ch.isalpha():
            word += ch.lower()
        else:
            if word:
                if ch in word_dict:
                    word_dict[ch] += 1
                else:
                    word_dict[ch] = 1
                total_words += 1
                word = ""
print("Нийт үгийн тоо:", total_words)