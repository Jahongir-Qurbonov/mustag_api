import json
from mutagen.id3 import Frames, Frames_2_2


def get_specs(frame: str) -> tuple[dict, dict]:
    """Returns a tuple of dicts containing the specs of the frame."""
    fr_spec = {}
    optional_spec = {}

    if frame in Frames:
        for fspec in Frames[frame]._framespec:
            fr_spec[fspec.__class__.__name__] = fspec
        for ospec in Frames[frame]._optionalspec:
            optional_spec[ospec.__class__.__name__] = ospec

    elif frame in Frames_2_2:
        for fspec in Frames_2_2[frame]._framespec:
            fr_spec[fspec.__class__.__name__] = fspec
        for ospec in Frames_2_2[frame]._optionalspec:
            optional_spec[ospec.__class__.__name__] = ospec

    return fr_spec, optional_spec


def get_all_specs():
    """Returns a tuple of dicts containing the specs of all frames."""
    fspecs = {}
    ospecs = {}

    for frame in Frames:
        fspcs = get_specs(frame)[0]
        ospcs = get_specs(frame)[1]

        for ospec in ospcs:
            if ospec not in ospecs:
                ospecs[ospec] = {
                    'spec': str(ospcs[ospec].__class__.__name__),
                }
                ospecs[ospec]['frames'] = []
            if ospec in ospecs:
                ospecs[ospec]['frames'].append(frame)

            # if ospec in fspecs:
            #     print(
            #         'Warning: Frame spec is both optionaland required:',
            #         frame, ospec,
            #     )

        for fspec in fspcs:
            if fspec not in fspecs:
                fspecs[fspec] = {
                    'spec': str(fspcs[fspec].__class__.__name__),
                }
                fspecs[fspec]['frames'] = []
            if fspec in fspecs:
                fspecs[fspec]['frames'].append(frame)

            # if fspec in ospecs:
            #     print(
            #         'Warning: Frame spec is both optional and required:',
            #         frame, fspec
            #     )

    return fspecs, ospecs


allspecs = get_all_specs()

a0 = allspecs[0]
a1 = allspecs[1]

with open('id3_help/specs/all_frame_specs.json', 'w') as f:
    json.dump(a0, f, indent=4)

with open('id3_help/specs/all_optional_specs.json', 'w') as f:
    json.dump(a1, f, indent=4)
