import json
import cc_data


def make_optional_fields_from_json(json_optional_fields):
    cc_fields = []
    for json_field in json_optional_fields:
        field_type = json_field["type"]
        if field_type == cc_data.CCMapTitleField.TYPE:
            cc_field = cc_data.CCMapTitleField(json_field["title"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCTrapControlsField.TYPE:
            cc_traps = []
            for json_trap in json_field["traps"]:
                bx = json_trap["button"][0]
                by = json_trap["button"][1]
                tx = json_trap["trap"][0]
                ty = json_trap["trap"][1]
                cc_traps.append(cc_data.CCTrapControl(bx, by, tx, ty))
            cc_field = cc_data.CCTrapControlsField(cc_traps)
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCCloningMachineControlsField.TYPE:
            cc_machines = []
            for json_machine in json_field["cloning_machines"]:
                bx = json_machine["button"][0]
                by = json_machine["button"][1]
                tx = json_machine["machine"][0]
                ty = json_machine["machine"][1]
                cc_machines.append(cc_data.CCCloningMachineControl(bx, by, tx, ty))
            cc_field = cc_data.CCCloningMachineControlsField(cc_machines)
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCEncodedPasswordField.TYPE:
            cc_field = cc_data.CCEncodedPasswordField(json_field["password"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCMapHintField.TYPE:
            cc_field = cc_data.CCMapHintField(json_field["hint"])
            cc_fields.append(cc_field)
        elif field_type == cc_data.CCMonsterMovementField.TYPE:
            cc_monsters = []
            for json_monster in json_field["monsters"]:
                x = json_monster[0]
                y = json_monster[1]
                cc_monsters.append(cc_data.CCCoordinate(x,y))
            cc_field = cc_data.CCMonsterMovementField(cc_monsters)
            cc_fields.append(cc_field)
        else:
            return None
    return cc_fields


def make_level_from_json(json_data):
    cc_level = cc_data.CCLevel()
    cc_level.level_number = json_data["level_number"]
    cc_level.time = json_data["time"]
    cc_level.num_chips = json_data["num_chips"]
    cc_level.upper_level = json_data["upper_level"]
    cc_level.lower_level = json_data["lower_level"]
    cc_level.optional_fields = make_optional_fields_from_json(json_data["optional_fields"])
    return cc_level


def make_cc_data_from_json(json_file):
    cc_dat_file = cc_data.CCDataFile()
    with open(json_file, 'r') as reader:
        json_data = json.load(reader)
        for json_level in json_data:
            cc_level = make_level_from_json(json_level)
            cc_dat_file.add_level(cc_level)
    return cc_dat_file
