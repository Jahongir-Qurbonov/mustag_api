from mutagen.id3 import Frames, Frames_2_2
import json

fr = 0
fr22 = 0
fr_d = {}
fr22_d = {}

with open('./id3_help/frames/mutagen_frames.txt', 'w') as f:
    for frame in Frames:
        f.write(frame + ' - ' + Frames[frame].__doc__ + '\n')
        fr += 1
with open('./id3_help/frames/mutagen_frames_2_2.txt', 'w') as f:
    for frame in Frames_2_2:
        f.write(frame + ' - ' + Frames_2_2[frame].__doc__ + '\n')
        fr22 += 1

rem: list[str] = [
    "FLAG23_ALTERTAG",
    "FLAG23_ALTERFILE",
    "FLAG23_READONLY",
    "FLAG23_COMPRESS",
    "FLAG23_ENCRYPT",
    "FLAG23_GROUP",

    "FLAG24_ALTERTAG",
    "FLAG24_ALTERFILE",
    "FLAG24_READONLY",
    "FLAG24_GROUPID",
    "FLAG24_COMPRESS",
    "FLAG24_ENCRYPT",
    "FLAG24_UNSYNCH",
    "FLAG24_DATALEN",

    "FrameID",
    "HashKey",
    "_framespec",
    "_optionalspec",

    "_fromData",
    "_get_v23_frame",
    "_merge_frame",
    "_pprint",
    "_readData",
    "_setattr",
    "_to_other",
    "_upgrade_frame",
    "_writeData",
    "pprint"
]

sep = [
    "append",
    "extend",
    "genres",
    "GENRES",
    "_channels",
]

with open('./id3_help/frames/mutagen_frames.json', 'w+') as f:
    for frame in Frames:
        fr_d[frame] = {"doc": Frames[frame].__doc__}
        fr_d[frame]['FrameID'] = Frames[frame].__name__
        # fr_d[frame]['HashKey'] = Frames[frame].HashKey

        fr_d[frame]['_framespec'] = {}
        for i in Frames[frame]._framespec:
            fr_d[frame]['_framespec'][i.name] = i.__class__.__name__

        fr_d[frame]['_optionalspec'] = {}
        for i in Frames[frame]._optionalspec:
            fr_d[frame]['_optionalspec'][i.name] = i.__class__.__name__

        # fr_d[frame]['__dir__'] = []
        # for d in dir(Frames[frame]):
        #     if not (d in rem or d.startswith('__')):
        #         fr_d[frame]['__dir__'].append(d)

        # if not (len(fr_d[frame]['__dir__']) == 0 or len(fr_d[frame]['__dir__']) == 2):
        #     print(frame, fr_d[frame]['__dir__'])

        if 'append' in dir(Frames[frame]):
            fr_d[frame]['append and extend'] = True

    json.dump(fr_d, f, indent=4)

with open('./id3_help/frames/mutagen_frames_2_2.json', 'w+') as f:
    for frame in Frames_2_2:
        fr22_d[frame] = {"doc": Frames_2_2[frame].__doc__}
        fr22_d[frame]['FrameID'] = Frames_2_2[frame].__name__
        # fr22_d[frame]['HashKey'] = Frames_2_2[frame].HashKey

        fr22_d[frame]['_framespec'] = {}
        for i in Frames_2_2[frame]._framespec:
            fr22_d[frame]['_framespec'][i.name] = i.__class__.__name__

        fr22_d[frame]['_optionalspec'] = {}
        for i in Frames_2_2[frame]._optionalspec:
            fr22_d[frame]['_optionalspec'][i.name] = i.__class__.__name__

        # fr22_d[frame]['__dir__'] = []
        # for d in dir(Frames_2_2[frame]):
        #     if not (d in rem or d.startswith('__')):
        #         fr22_d[frame]['__dir__'].append(d)

        # if not (len(fr22_d[frame]['__dir__']) == 0 or len(fr22_d[frame]['__dir__']) == 2):
        #     print(frame, fr22_d[frame]['__dir__'])

        if 'append' in dir(Frames_2_2[frame]):
            fr22_d[frame]['append'] = True

    json.dump(fr22_d, f, indent=4)

print(fr, fr22)
