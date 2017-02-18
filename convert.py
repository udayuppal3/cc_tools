import cc_dat_utils
import cc_json_utils
import sys

# print(str(cc_dat_utils.make_cc_data_from_dat("data/pfgd_test.dat")))

default_input_json_file = "data/uuppal_cc1.json"
default_output_dat_file = "data/uuppal_cc1.dat"

if len(sys.argv) == 3:
    input_json_file = sys.argv[1]
    output_dat_file = sys.argv[2]
    print("Using command line args:", input_json_file, output_dat_file)
else:
    print("Unknown command line options. Using default values:", default_input_json_file, default_output_dat_file)
    input_json_file = default_input_json_file
    output_dat_file = default_output_dat_file

json_data = cc_json_utils.make_cc_data_from_json(input_json_file)
cc_dat_utils.write_cc_data_to_dat(json_data, output_dat_file)
dat_data = cc_dat_utils.make_cc_data_from_dat(output_dat_file)
print(dat_data)