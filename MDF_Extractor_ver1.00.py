#-------------------------------------------------------------------------------
# Name:        MDF Extractor
# Author:      Naoshi Nishihashi
# Created:     14/07/2022
#
# Licence:     GPL v3
# ----------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
# ----------------------------------------------------------------------
#-------------------------------------------------------------------------------

import mdfreader
import pickle

def main():
    csv_flag = 1
    path_config = 'Configuration.cfg'
    with open(path_config) as f_r_cfg:
        cfg_line = f_r_cfg.readlines()

    data_file_path = cfg_line[0].replace('\n','')
    csv_flag = int(cfg_line[1].replace('\n',''))
    sample_time_step = float(cfg_line[2].replace('\n',''))

    # Read MDF File
    extract_data = mdfreader.Mdf(data_file_path)

    state = 'finish'

    if csv_flag == 1:
        try:
            extract_data.export_to_csv(file_name= 'ExtractData.csv', sampling = float(sample_time_step))
        except:
            state = 'error'
    else:
        temp_dict = {}
        for key in extract_data.masterChannelList:
            temp_dict[key] = extract_data.return_pandas_dataframe(key)

        try:
            with open('ExtractData.pkl', 'wb') as f:
                pickle.dump(temp_dict, f)
        except:
            state = 'error'

    return state


if __name__ == '__main__':
    main()
