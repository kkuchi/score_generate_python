import mido, random
from mido import Message, MidiFile, MidiTrack, MetaMessage

# 1小節分 ランダムで8分の音符(1)か休符(0)かを決める
def measure():
	list = [random.random() for a in range(0,8)]
	list = [1 if i>0.5 else 0 for i in list]
	return list

# midiファイル、トラック作成 テンポ設定
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(120)))

# 8小節のランダム譜面作成
res = []
for i in range(0,8):
	res.append(measure())
# 確認でprint
print(res)

# 1ならvelocity=127で音符、0ならvelocity=0で休符を入れる
# デフォルトはtimeが480で四分音符なので、240で8分音符になる
# timeは最後の入力からの相対時間
for i in res:
	for j in i:
		if j == 1:
			track.append(Message('note_on', note=72, velocity=127, time=0))
			track.append(Message('note_off', note=72, time=240))
		else:
			track.append(Message('note_on', note=72, velocity=0, time=0))
			track.append(Message('note_off', note=72, time=240))


mid.save('new_song.mid')