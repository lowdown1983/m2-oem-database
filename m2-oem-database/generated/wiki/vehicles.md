# Vehicle message catalog (opendbc harvest)

Mechanically harvested from commaai/opendbc. Grade B: real captures, but comma.ai's ADAS-driving subset — not complete vehicle databases, 2016+ focused.
Signal-level decode (start bit, length, byte order, factor, offset, unit) lives in `generated/json/vehicles.json` and the per-message RAG chunks; the wiki shows the signal count per message.

## gm_global_a_chassis — GM Global A platform [B]

- Make: gm; Chassis bus; Global A underpins most 2010+ GM vehicles
- Messages: 4; signals: 9
- Evidence: opendbc/opendbc/dbc/gm_global_a_chassis.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 823 | 0x337 | PACMParkAssitCmd | 7 | 3 |
| 560 | 0x230 | EBCMRegen | 6 | 1 |
| 368 | 0x170 | EBCMFrictionBrakeStatus | 8 | 1 |
| 789 | 0x315 | EBCMFrictionBrakeCmd | 5 | 4 |

## gm_global_a_high_voltage_management — GM Global A platform [B]

- Make: gm; Hybrid/EV high-voltage management
- Messages: 12; signals: 120
- Evidence: opendbc/opendbc/dbc/gm_global_a_high_voltage_management.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 512 | 0x200 | Battery_Module_1 | 8 | 24 |
| 514 | 0x202 | Battery_Module_2 | 8 | 24 |
| 516 | 0x204 | Battery_Module_3 | 8 | 24 |
| 518 | 0x206 | Battery_Module_4 | 8 | 24 |
| 528 | 0x210 | Pack_Stats | 8 | 2 |
| 530 | 0x212 | Charger_stats | 6 | 4 |
| 770 | 0x302 | Battery_temp | 8 | 9 |
| 782 | 0x30e | Charger_Command | 1 | 1 |
| 772 | 0x304 | Charger_parameters | 4 | 3 |
| 1120 | 0x460 | Coolant_Temp | 4 | 2 |
| 778 | 0x30a | AC_Stats | 7 | 2 |
| 776 | 0x308 | Charger_status | 5 | 1 |

## gm_global_a_lowspeed — GM Global A platform [B]

- Make: gm; Low-speed GMLAN bus
- Messages: 13; signals: 27
- Evidence: opendbc/opendbc/dbc/gm_global_a_lowspeed.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 274923520 | 0x10630000 | DriverDoorStatus | 1 | 1 |
| 272629760 | 0x10400000 | Chime | 5 | 5 |
| 270581760 | 0x1020c000 | BlinkerStatus | 5 | 3 |
| 270794752 | 0x10240000 | SteeringWheelAngle | 8 | 1 |
| 271368192 | 0x102cc000 | GearShifter | 8 | 1 |
| 271360000 | 0x102ca000 | GasPedalRegenCruise | 8 | 4 |
| 270860288 | 0x10250000 | BrakePedal | 2 | 2 |
| 275480576 | 0x106b8000 | WheelSpeed | 8 | 4 |
| 270598144 | 0x10210000 | VehicleSpeed | 8 | 2 |
| 276135936 | 0x10758000 | CruiseButtons | 3 | 1 |
| 276127744 | 0x10756000 | CruiseButtons2 | 1 | 1 |
| 275955897 | 0x1072c0b9 | LeftRadar | 2 | 1 |
| 275980379 | 0x1073205b | RightRadar | 2 | 1 |

## gm_global_a_lowspeed_1818125 — GM Global A platform [B]

- Make: gm; Low-speed GMLAN, extended ID variant
- Messages: 367; signals: 3210
- Evidence: opendbc/opendbc/dbc/gm_global_a_lowspeed_1818125.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 2152177664 | 0x8047a000 | OTA_Electric_Pwr_Readiness_LS | 1 | 1 |
| 2152013824 | 0x80452000 | Smart_High_Beam_Cust_LS | 1 | 2 |
| 2159255552 | 0x80b3a000 | ODI_CenterStack_2_BCM_LS | 8 | 1 |
| 2159247360 | 0x80b38000 | ODI_BCM_2_CenterStack_LS | 8 | 1 |
| 2152046592 | 0x8045a000 | Remote_Climate_Control_Req_LS | 5 | 10 |
| 2152030208 | 0x80456000 | Tuner_Frequency_Request_LS | 8 | 2 |
| 2150531072 | 0x802e8000 | Regen_Power_Ind_LS | 4 | 3 |
| 2151833600 | 0x80426000 | Heated_Wndshild_CstmrIhbt_Req_LS | 1 | 2 |
| 2151817216 | 0x80422000 | Heated_Wndshild_Cstmr_Req_LS | 1 | 1 |
| 2151849984 | 0x8042a000 | Seat_Level_Setting_Request_LS | 2 | 4 |
| 2153897984 | 0x8061e000 | ARB_OpMode_Customization_LS | 1 | 3 |
| 2151702528 | 0x80406000 | Lane_Keeping_Assist_LS | 2 | 5 |
| 2156986368 | 0x80910000 | PassPhrase_3_AMM_LS | 8 | 1 |
| 2156978176 | 0x8090e000 | PassPhrase_2_AMM_LS | 8 | 1 |
| 2156969984 | 0x8090c000 | PassPhrase_1_AMM_LS | 8 | 1 |
| 2150236160 | 0x802a0000 | Unlock_Key_Store_Crypt_2_LS | 8 | 3 |
| 2150170624 | 0x80290000 | Unlock_Key_Store_Crypt_1_LS | 8 | 3 |
| 2155126784 | 0x8074a000 | Drvr_Seat_Rearward_Movmnt_LS | 1 | 1 |
| 2154725376 | 0x806e8000 | Auxiliary_Heater_LS | 1 | 2 |
| 2157051904 | 0x80920000 | WiFi_Station_AMM_LS | 5 | 3 |
| 2156994560 | 0x80912000 | WiFi_AP_Data_AMM_LS | 2 | 4 |
| 2158133248 | 0x80a28000 | Hill_Top_Customization_LS | 6 | 12 |
| 2154651648 | 0x806d6000 | Telematics_Audio_Control_LS | 1 | 3 |
| 2154635264 | 0x806d2000 | Telematics_Audio_Request_LS | 1 | 3 |
| 2152529920 | 0x804d0000 | LVM_Audio_Video_Command_LS | 2 | 7 |
| 2152513536 | 0x804cc000 | LVM_Audio_Video_Req_LS | 2 | 5 |
| 2154889216 | 0x80710000 | Cluster_HMI_Animation_Req_LS | 1 | 1 |
| 2154872832 | 0x8070c000 | Infotainment_Activation_Req_LS | 1 | 2 |
| 2156961792 | 0x8090a000 | SSID_AMM_3_LS | 8 | 1 |
| 2154569728 | 0x806c2000 | Infotainment_System_State_LS | 1 | 1 |
| 2151931904 | 0x8043e000 | Custom_Launch_Ctrl_LS | 8 | 25 |
| 2150244352 | 0x802a2000 | HMI_EngyConsmpHistGrph_1_LS | 8 | 12 |
| 2156953600 | 0x80908000 | SSID_AMM_2_LS | 8 | 1 |
| 2151686144 | 0x80402000 | SD_Card_LS | 2 | 3 |
| 2155028480 | 0x80732000 | Lane_Change_Threat_LS | 2 | 2 |
| 2151915520 | 0x8043a000 | HMI_Display_LS | 8 | 24 |
| 2152153088 | 0x80474000 | Right_Rear_Seat_Display_Stats_LS | 6 | 20 |
| 2152136704 | 0x80470000 | Right_Rear_Seat_Massage_LS | 8 | 18 |
| 2152120320 | 0x8046c000 | Right_Rear_Seat_Actuator_LS | 8 | 17 |
| 2152103936 | 0x80468000 | Left_Rear_Seat_Display_Status_LS | 6 | 20 |
| 2152087552 | 0x80464000 | Left_Rear_Seat_Massage_LS | 8 | 18 |
| 2152071168 | 0x80460000 | Left_Rear_Seat_Actuator_LS | 8 | 17 |
| 2153947136 | 0x8062a000 | Remote_Reflash_Stat_LS | 1 | 1 |
| 2152628224 | 0x804e8000 | OnBoard_Tester_Response_LS | 2 | 4 |
| 2152112128 | 0x8046a000 | Performanc_Mode_Vis_Scrn_Stat_LS | 5 | 13 |
| 2152775680 | 0x8050c000 | Front_360_Camera_On_LS | 3 | 17 |
| 2153857024 | 0x80614000 | Teen_Driver_Event_Report_2_LS | 8 | 19 |
| 2153865216 | 0x80616000 | Teen_Driver_Customization_Req_LS | 4 | 7 |
| 2153840640 | 0x80610000 | Teen_Driver_Event_Report_1_LS | 8 | 8 |
| 2153824256 | 0x8060c000 | Teen_Driver_Control_Info_LS | 8 | 17 |
| 2155151360 | 0x80750000 | Psngr_Seat_Massage_Priority_LS | 8 | 18 |
| 2155134976 | 0x8074c000 | Psngr_Seat_Control_Disp_Stat_LS | 6 | 21 |
| 2155118592 | 0x80748000 | Psngr_Seat_Actuator_Priority_LS | 8 | 17 |
| 2155102208 | 0x80744000 | Driver_Seat_Massage_Priority_LS | 8 | 18 |
| 2155085824 | 0x80740000 | Driver_Seat_Control_Disp_Stat_LS | 8 | 24 |
| 2155069440 | 0x8073c000 | Driver_Seat_Actuator_Priority_LS | 8 | 17 |
| 2156937216 | 0x80904000 | PassPhrase_Digits_17_to_24_LS | 8 | 1 |
| 2156929024 | 0x80902000 | PassPhrase_Digits_9_to_16_LS | 8 | 1 |
| 2156920832 | 0x80900000 | PassPhrase_Digits_1_to_8_LS | 8 | 1 |
| 2156871680 | 0x808f4000 | SSID_Digits_17_to_24_LS | 8 | 1 |
| 2156863488 | 0x808f2000 | SSID_Digits_9_to_16_LS | 8 | 1 |
| 2156855296 | 0x808f0000 | SSID_Digits_1_to_8_LS | 8 | 1 |
| 2152480768 | 0x804c4000 | Perfr_Data_Recorder_Lap_Info_LS | 6 | 8 |
| 2152497152 | 0x804c8000 | Perf_Data_Recroder_RT_Info_LS | 4 | 6 |
| 2153791488 | 0x80604000 | ARB_State_LS | 1 | 1 |
| 2149883904 | 0x8024a000 | BluetoothTetheringPairingRsp_LS | 7 | 4 |
| 2150252544 | 0x802a4000 | HMI_EngyConsmpHistGrph_LS | 8 | 15 |
| 2150391808 | 0x802c6000 | HMI_Hourmeter_Data_LS | 6 | 2 |
| 2155913216 | 0x8080a000 | Diesel_Information_2_LS | 7 | 17 |
| 2034 | 0x7f2 | CCP_Data_Transmission_Object_LS | 8 | 1 |
| 2032 | 0x7f0 | CCP_Command_Receive_Object_LS | 8 | 1 |
| 2152095744 | 0x80466000 | HSGMLAN_Customization_Setings_LS | 5 | 35 |
| 2156945408 | 0x80906000 | SSID_AMM_1_LS | 8 | 1 |
| 2152611840 | 0x804e4000 | OnBoard_Tester_Request_LS | 2 | 5 |
| 2153308160 | 0x8058e000 | Hyb_Redundant_Batt_Data2_LS | 4 | 8 |
| 2155970560 | 0x80818000 | HVAC_PowerManager_Status_LS | 1 | 2 |
| 2151178240 | 0x80386000 | Lighting_Customization_Rqst_1_LS | 4 | 8 |
| 2154790912 | 0x806f8000 | Lighting_Customization_Info_2_LS | 2 | 8 |
| 2151292928 | 0x803a2000 | V2V_Customization_Menu_LS | 5 | 30 |
| 2151464960 | 0x803cc000 | V2V_Warnings_LS | 5 | 10 |
| 2151448576 | 0x803c8000 | V2V_Seat_Vib_Request_LS | 3 | 6 |
| 2153930752 | 0x80626000 | Lane_Centering_Convenience_LS | 3 | 9 |
| 2153889792 | 0x8061c000 | Lane_Centering_Arrow_LS | 5 | 9 |
| 2153914368 | 0x80622000 | Energy_Usage_LS | 7 | 9 |
| 2151882752 | 0x80432000 | PTO_Customization_Request_LS | 3 | 5 |
| 2151899136 | 0x80436000 | PTO_Status_LS | 5 | 27 |
| 2150580224 | 0x802f4000 | HMI_UtlChrgIntrfr_Indication_LS | 5 | 5 |
| 2151735296 | 0x8040e000 | Rear_Cross_Traffic_Alert_Ind_LS | 1 | 7 |
| 2151792640 | 0x8041c000 | Rear_Cross_Traffic_Alert_Rght_LS | 5 | 5 |
| 2149826560 | 0x8023c000 | FCA_VisionBased_Info_2_LS | 4 | 15 |
| 2149957632 | 0x8025c000 | Park_Assist_ESSprocess_Info_LS | 1 | 4 |
| 2149941248 | 0x80258000 | Park_Assist_ESSbased_Info_LS | 5 | 13 |
| 2156314624 | 0x8086c000 | High_Volt_Time_Based_Chrg_LS | 8 | 21 |
| 2150449152 | 0x802d4000 | Engine_Information_5_LS | 4 | 23 |
| 2149810176 | 0x80238000 | FCA_VisionBased_Info_1_LS | 1 | 2 |
| 2149793792 | 0x80234000 | FCA_VisionBased_Info_LS | 6 | 6 |
| 2150080512 | 0x8027a000 | Aux_Coolant_Heater_Status_LS | 8 | 21 |
| 2153873408 | 0x80618000 | Heated_Steering_Whl_Rqsted_LS | 1 | 1 |
| 2152128512 | 0x8046e000 | Performance_Mode_Cust_Setings_LS | 4 | 29 |
| 2151997440 | 0x8044e000 | Driver_Drowsiness_Dtctn_Stat_LS | 5 | 5 |
| 2156331008 | 0x80870000 | High_Voltage_EnergyMgmt_Ctrl_LS | 7 | 4 |
| 2151776256 | 0x80418000 | Rear_Cross_Traffic_Alert_Left_LS | 5 | 5 |
| 2154774528 | 0x806f4000 | Lighting_Customization_Info_1_LS | 1 | 4 |
| 2150375424 | 0x802c2000 | Eng_Maintenance_Mode_Strt_Req_LS | 3 | 11 |
| 2150383616 | 0x802c4000 | Engine_Maintenance_Mode_Req_LS | 8 | 8 |
| 2151981056 | 0x8044a000 | Drive_Cycle_Efficiency_LS | 8 | 5 |
| 2151964672 | 0x80446000 | Drive_Cycle_Energy_Efficiency_LS | 8 | 6 |
| 2156298240 | 0x80868000 | High_Volt_Batt_Time_Pwr_Chrg_LS | 8 | 24 |
| 2149924864 | 0x80254000 | Drv_Pref_Mode_Switch_Status_LS | 8 | 57 |
| 2152054784 | 0x8045c000 | HMI_Disp_Hyb_Animation_Status_LS | 1 | 3 |
| 2150301696 | 0x802b0000 | HMI_Animation_Initiator_LS | 1 | 1 |
| 2150563840 | 0x802f0000 | HMI_AnimationHybridRadio_LS | 3 | 4 |
| 2154758144 | 0x806f0000 | Auxiliary_Heater_Active_LS | 1 | 1 |
| 2154577920 | 0x806c4000 | Amp_Sink_Stat_LS | 2 | 14 |
| 2154594304 | 0x806c8000 | Amp_Settings_Tone_Ctrl_LS | 5 | 11 |
| 2154586112 | 0x806c6000 | Amp_Settings_Sink_Lvl_Ctrl_LS | 8 | 12 |
| 2152857600 | 0x80520000 | ACC_TrafficJam_RouteSpd_Stat_LS | 3 | 5 |
| 2158149632 | 0x80a2c000 | High_Volt_Bat_Time_Bsd_Rsp_1_LS | 7 | 16 |
| 2158116864 | 0x80a24000 | High_Volt_Bat_Time_Bsd_Rsp_LS | 8 | 16 |
| 2156281856 | 0x80864000 | High_Volt_Bat_Time_Bsd_Req_1_LS | 7 | 19 |
| 2156265472 | 0x80860000 | High_Volt_Bat_Time_Bsd_Req_LS | 8 | 20 |
| 2150113280 | 0x80282000 | Energy_Storage_System_LS | 8 | 5 |
| 2150055936 | 0x80274000 | Climate_Control_Status_LS | 5 | 4 |
| 2150039552 | 0x80270000 | Thrml_Ref_Compressor_Status_LS | 5 | 8 |
| 2154856448 | 0x80708000 | Humidity_Sensor_Status_LS | 5 | 3 |
| 2151342080 | 0x803ae000 | Park_Assistant_Right_Status_LS | 2 | 4 |
| 2151325696 | 0x803aa000 | Park_Assistant_Left_Status_LS | 2 | 4 |
| 2151809024 | 0x80420000 | Drv_Cycl_Elec_Enrgy_Consumd_LS | 8 | 7 |
| 2151858176 | 0x8042c000 | Drv_Cycl_Elec_Enrgy_States_LS | 8 | 4 |
| 2150547456 | 0x802ec000 | HMI_Hybrid_Vehicle_Status_LS | 8 | 22 |
| 2151489536 | 0x803d2000 | CSV_EOCM_R_Indications_LS | 1 | 3 |
| 2149761024 | 0x8022c000 | Chassis_Information_2_LS | 6 | 13 |
| 2155012096 | 0x8072e000 | SBZA_Right_Status_LS | 1 | 8 |
| 2150514688 | 0x802e4000 | Power_Slidining_Door_Status_LS | 1 | 4 |
| 2158067712 | 0x80a18000 | Video_Master_Info_2_LS | 5 | 7 |
| 2158051328 | 0x80a14000 | Video_Master_Info_1_LS | 5 | 8 |
| 2158034944 | 0x80a10000 | TV_Tuner_Info_LS | 6 | 11 |
| 2158018560 | 0x80a0c000 | TV_Station_Name_LS | 8 | 1 |
| 2156838912 | 0x808ec000 | WiFi_Station_LS | 7 | 3 |
| 2156822528 | 0x808e8000 | WiFi_AP_Data_LS | 2 | 4 |
| 2151948288 | 0x80442000 | Driver_Drow_Det_Cst_Rqst_LS | 1 | 2 |
| 2158002176 | 0x80a08000 | XM_Radio_Service_LS | 1 | 2 |
| 2149728256 | 0x80224000 | Charging_Sys_Trans_Shift_Lock_LS | 5 | 17 |
| 2150023168 | 0x8026c000 | Hybrid_Information_LS | 5 | 6 |
| 2153988096 | 0x80634000 | Power_Elec_Info_LS | 7 | 10 |
| 2155945984 | 0x80812000 | Jump_Start_Req_LS | 1 | 4 |
| 2155585536 | 0x807ba000 | MSB_Customization_Setting_Req_LS | 1 | 1 |
| 2155569152 | 0x807b6000 | CPS_Customization_Setting_Req_LS | 3 | 6 |
| 2155233280 | 0x80764000 | VICM_Info_LS | 8 | 12 |
| 2152169472 | 0x80478000 | Coolant_Heater_Status_LS | 3 | 8 |
| 2152759296 | 0x80508000 | SITM_Front_Sensor_IO_LS | 1 | 5 |
| 2152742912 | 0x80504000 | SITM_Rear_Sensor_IO_LS | 1 | 4 |
| 2150891520 | 0x80340000 | Go_Notifier_Req_LS | 5 | 12 |
| 2151751680 | 0x80412000 | Haptic_Seat_Status_LS | 3 | 4 |
| 2155536384 | 0x807ae000 | Rear_Virtual_Bmper_Indication_LS | 1 | 6 |
| 2151481344 | 0x803d0000 | CSV_FSRACC_Indications_LS | 1 | 5 |
| 2151432192 | 0x803c4000 | ACC_Drv_Seat_Vib_Req_IO_LS | 1 | 2 |
| 2151415808 | 0x803c0000 | Ln_Dep_Wrn_Drv_Seat_Vib_Req_LS | 5 | 10 |
| 2151350272 | 0x803b0000 | Frnt_Prk_Ast_Drv_Seat_Vib_Req_LS | 3 | 4 |
| 2151333888 | 0x803ac000 | Rear_Prk_Ast_Drv_Seat_Vib_Req_LS | 1 | 2 |
| 2151522304 | 0x803da000 | Reset_FuelLife_Request_LS | 1 | 4 |
| 2150629376 | 0x80300000 | CV_System_Failure_LS | 1 | 1 |
| 2155929600 | 0x8080e000 | Diesel_Information_LS | 8 | 11 |
| 2154741760 | 0x806ec000 | RSA_Status_LS | 1 | 1 |
| 2154807296 | 0x806fc000 | Lighting_Customization_Info_3_LS | 4 | 17 |
| 2151079936 | 0x8036e000 | PDIM_Status_LS | 1 | 1 |
| 2155364352 | 0x80784000 | Hybrid_Information_SuperSlow_LS | 5 | 9 |
| 2154979328 | 0x80726000 | Front_Seat_Heat_Cool_Req_LS | 1 | 1 |
| 2155282432 | 0x80770000 | RearSeat_HeatVent_Cool_LS | 1 | 1 |
| 2151505920 | 0x803d6000 | VehInfoTripComputer_LS | 7 | 11 |
| 2155896832 | 0x80806000 | Alternative_Fuel_Information_LS | 5 | 13 |
| 2155552768 | 0x807b2000 | Exterior_Lock_Switch_Req_LS | 1 | 1 |
| 2154496000 | 0x806b0000 | Rear_Closure_Soft_Top_Info_LS | 1 | 4 |
| 2155208704 | 0x8075e000 | Power_Conv_Top_Info_LS | 3 | 20 |
| 2153390080 | 0x805a2000 | Manual_Liftgate_Control_LS | 1 | 3 |
| 2155175936 | 0x80756000 | CruiseControlGapSwitch_LS | 1 | 2 |
| 2156806144 | 0x808e4000 | Cellular_Network_Date_and_Time | 6 | 13 |
| 2154078208 | 0x8064a000 | Window_Position_Status_LS | 2 | 4 |
| 2159058944 | 0x80b0a000 | ODIEvent_IPC_LS | 3 | 4 |
| 2159042560 | 0x80b06000 | ODI_DynData_IPC_LS | 8 | 6 |
| 2150006784 | 0x80268000 | System_Power_Mode_Pushbutton_LS | 1 | 4 |
| 2155216896 | 0x80760000 | Road_Type_Information_LS | 6 | 17 |
| 2156216320 | 0x80854000 | TTY_Status_LS | 1 | 1 |
| 2158813184 | 0x80ace000 | ODIIndication_IPC_LS | 8 | 58 |
| 2150277120 | 0x802aa000 | GPS_Geographical_Position_LS | 8 | 6 |
| 2150285312 | 0x802ac000 | GPS_Elevation_and_Heading_LS | 8 | 12 |
| 2151890944 | 0x80434000 | Telematics_Indication_Request_LS | 4 | 6 |
| 2151251968 | 0x80398000 | Telematics_Indication_Control_LS | 4 | 6 |
| 2155495424 | 0x807a4000 | Remote_Start_Seat_Request_LS | 1 | 2 |
| 2149990400 | 0x80264000 | HS_Indications_Fast_LS | 8 | 24 |
| 2155380736 | 0x80788000 | HS_Indications_SuperSlow_LS | 6 | 25 |
| 2150498304 | 0x802e0000 | Analog_Values_Slow_LS | 8 | 22 |
| 2151047168 | 0x80366000 | HUD_Status_LS | 1 | 2 |
| 2155331584 | 0x8077c000 | Wheel_Pulses_LS | 4 | 3 |
| 2154225664 | 0x8066e000 | Door_Handle_Switch_Status_LS | 1 | 5 |
| 2149900288 | 0x8024e000 | Telematics_Contol_LS | 3 | 7 |
| 2159001600 | 0x80afc000 | ODIEnumDynamicData_IPC_LS | 8 | 20 |
| 2158993408 | 0x80afa000 | ODIEnumDynamicData_CntrStack_LS | 8 | 20 |
| 2154708992 | 0x806e4000 | Audio_Master_Source_Status_LS | 2 | 4 |
| 2158985216 | 0x80af8000 | ODIDynDataMultiReq_OTIM_LS | 8 | 13 |
| 2154471424 | 0x806aa000 | Rear_Closure_Ajar_Switch_Status | 1 | 2 |
| 2159149056 | 0x80b20000 | ODI_TEL_2_CenterStack_LS | 8 | 1 |
| 2159116288 | 0x80b18000 | ODI_TEL_2_AuxIP_LS | 8 | 1 |
| 2158796800 | 0x80aca000 | ODIIndication_LS | 8 | 58 |
| 2158755840 | 0x80ac0000 | ODIEvent_LS | 4 | 4 |
| 2159157248 | 0x80b22000 | ODI_CenterStack_2_TEL_LS | 8 | 1 |
| 2153955328 | 0x8062c000 | Infrastructure_Timer_Status_LS | 5 | 5 |
| 2151063552 | 0x8036a000 | Infotainment_Operation_LS | 7 | 15 |
| 2157985792 | 0x80a04000 | Fob_Programming_Request_LS | 1 | 1 |
| 2151284736 | 0x803a0000 | Park_Assistant_General_Status | 1 | 7 |
| 2159099904 | 0x80b14000 | ODI_DAB_2_AuxIP_LS | 8 | 1 |
| 2159067136 | 0x80b0c000 | ODI_DAB_2_IPC_LS | 8 | 1 |
| 2159206400 | 0x80b2e000 | ODI_AuxIP_2_IPC_LS | 8 | 1 |
| 2159198208 | 0x80b2c000 | ODI_IPC_2_AuxIP_LS | 8 | 1 |
| 2159190016 | 0x80b2a000 | ODI_AuxIP_2_CenterStack_LS | 8 | 1 |
| 2159181824 | 0x80b28000 | ODI_CenterStack_2_AuxIP_LS | 8 | 1 |
| 2159173632 | 0x80b26000 | ODI_IPC_2_CenterStack_LS | 8 | 1 |
| 2159165440 | 0x80b24000 | ODI_CenterStack_2_IPC_LS | 8 | 1 |
| 2159108096 | 0x80b16000 | ODI_AuxIP_2_DAB_LS | 8 | 1 |
| 2159075328 | 0x80b0e000 | ODI_IPC_2_DAB_LS | 8 | 1 |
| 2151718912 | 0x8040a000 | Chime_Active | 1 | 2 |
| 2155479040 | 0x807a0000 | Customization_Setting_Request_LS | 5 | 12 |
| 2151383040 | 0x803b8000 | Reset_TP_request_LS | 1 | 1 |
| 2155421696 | 0x80792000 | Passive_Entry_Challenge_LS | 5 | 5 |
| 2155413504 | 0x80790000 | Drv_Dr_Key_Cyl_Status_LS | 3 | 5 |
| 2159026176 | 0x80b02000 | ODIDynamicData_LS | 8 | 6 |
| 2158936064 | 0x80aec000 | ODIEnumDynamicData_LS | 8 | 20 |
| 2158845952 | 0x80ad6000 | ODIAction_CntrStack_LS | 8 | 6 |
| 2158886912 | 0x80ae0000 | ODIDynDataListRequest_IPC_LS | 8 | 11 |
| 2151366656 | 0x803b4000 | Man_Prk_Brk_LS | 1 | 6 |
| 2149842944 | 0x80240000 | Vehicle_Stability_LS | 8 | 19 |
| 2159132672 | 0x80b1c000 | ODIAction_RearSeat_LS | 8 | 6 |
| 2158968832 | 0x80af4000 | ODI_RearSeat_2_Centerstack_LS | 8 | 1 |
| 2158960640 | 0x80af2000 | ODIIndication_Centerstack_LS | 8 | 58 |
| 2158977024 | 0x80af6000 | ODIEvent_Centerstack_LS | 4 | 4 |
| 2158952448 | 0x80af0000 | ODIDynDataMultiReq_RearSeat_LS | 8 | 13 |
| 2158944256 | 0x80aee000 | ODIDynDataListReq_RearSeat_LS | 8 | 11 |
| 2158927872 | 0x80aea000 | ODI_DynData_CenterStack_LS | 8 | 6 |
| 2158895104 | 0x80ae2000 | ODI_CenterStack_2_RearSeat_LS | 8 | 1 |
| 2152038400 | 0x80458000 | Infomatics_Response_Payload_LS | 8 | 1 |
| 2152022016 | 0x80454000 | Infomatics_Metadata_Response_LS | 7 | 7 |
| 2152005632 | 0x80450000 | Infomatics_Request_Payload_LS | 8 | 1 |
| 2151989248 | 0x8044c000 | Infomatics_Metadata_Request_LS | 5 | 3 |
| 2151972864 | 0x80448000 | Fuel_Level_Status_LS | 4 | 7 |
| 2154528768 | 0x806b8000 | Wheel_Grnd_Velocity_LS | 8 | 12 |
| 2150916096 | 0x80346000 | Park_Heater_Info_LS | 4 | 10 |
| 2150367232 | 0x802c0000 | Immobilizer_Identifier_LS | 5 | 4 |
| 2150621184 | 0x802fe000 | Keyless_Start_Auth_LS | 1 | 9 |
| 2151309312 | 0x803a6000 | Inflatable_Restraints_Key_Id_LS | 2 | 1 |
| 2154061824 | 0x80646000 | Window_Normalized_Indication_LS | 1 | 7 |
| 2154512384 | 0x806b4000 | Rear_Closure_Rel_Sw_Sta_LS | 1 | 3 |
| 2155347968 | 0x80780000 | HS_Indications_Slow_LS | 8 | 45 |
| 2149777408 | 0x80230000 | Non_Drvn_Whl_Rot_Status_LS | 8 | 14 |
| 2149769216 | 0x8022e000 | Driven_Whl_Rotational_Stat_LS | 8 | 14 |
| 2156789760 | 0x808e0000 | Time_of_Day_LS | 6 | 10 |
| 2155020288 | 0x80730000 | Language_Selection_LS | 1 | 2 |
| 2150432768 | 0x802d0000 | Engine_Information_4_LS | 8 | 17 |
| 2155298816 | 0x80774000 | Tire_Pressure_Sensor_Prog_Req_LS | 1 | 2 |
| 2158878720 | 0x80ade000 | ODIDynDataListReq_CntrStack_LS | 8 | 11 |
| 2158870528 | 0x80adc000 | ODIDynDataListRequest_AuxIP_LS | 8 | 11 |
| 2154692608 | 0x806e0000 | Audio_Source_Status_LS | 2 | 5 |
| 2154627072 | 0x806d0000 | Audio_Master_Arbitration_Command | 2 | 4 |
| 2151112704 | 0x80376000 | Occupant_Sensning_Status_LS | 2 | 7 |
| 2153938944 | 0x80628000 | Remote_Reflash_Req_LS | 1 | 1 |
| 2159239168 | 0x80b36000 | ODI_TEL_2_OTIM_LS | 8 | 1 |
| 2159230976 | 0x80b34000 | ODI_OTIM_2_TEL_LS | 8 | 1 |
| 2159222784 | 0x80b32000 | ODI_PDIM_2_CenterStack_LS | 8 | 1 |
| 2159214592 | 0x80b30000 | ODI_CenterStack_2_PDIM_LS | 8 | 1 |
| 2158862336 | 0x80ada000 | ODIAction_OTIM_LS | 8 | 6 |
| 2150662144 | 0x80308000 | Environment_Id_Resp_3_LS | 3 | 2 |
| 2150653952 | 0x80306000 | Environment_Id_Resp_2_LS | 3 | 2 |
| 2150850560 | 0x80336000 | Seatbelt_Information_LS | 1 | 6 |
| 2154659840 | 0x806d8000 | Column_Lock_Status_2 | 2 | 8 |
| 2154938368 | 0x8071c000 | Fob_Programming_Mode_Status_LS | 1 | 1 |
| 2155266048 | 0x8076c000 | Rear_Seat_Heat_Cool_Switches_LS | 1 | 6 |
| 2155249664 | 0x80768000 | Rear_Seat_Heat_Cool_Control_LS | 4 | 24 |
| 2155184128 | 0x80758000 | CruiseControl_LS | 3 | 17 |
| 2155167744 | 0x80754000 | Power_Mode_Info_LS | 3 | 21 |
| 2154921984 | 0x80718000 | Fob_Status_LS | 2 | 5 |
| 2151317504 | 0x803a8000 | Park_Assistant_Rear_Status | 4 | 6 |
| 2151301120 | 0x803a4000 | Park_Assistant_Front_Status | 4 | 8 |
| 2159083520 | 0x80b10000 | ODI_TEL_2_IPC_LS | 8 | 1 |
| 2153922560 | 0x80624000 | Climate_Control_Voltage_LS | 3 | 7 |
| 2153807872 | 0x80608000 | Door_Open_Switch_Status_LS | 1 | 8 |
| 2150703104 | 0x80312000 | Audio_Amplifier_Status | 1 | 3 |
| 2151399424 | 0x803bc000 | Wash_Level_LS | 1 | 1 |
| 2151956480 | 0x80444000 | Driver_Workload_LS | 2 | 4 |
| 2151940096 | 0x80440000 | Alarm_2_Request_LS | 7 | 12 |
| 2151923712 | 0x8043c000 | Alarm_1_Request_LS | 5 | 13 |
| 2150645760 | 0x80304000 | Environment_Id_Resp_1_LS | 3 | 2 |
| 2152464384 | 0x804c0000 | Lane_Departure_Warning_LS | 3 | 18 |
| 2154971136 | 0x80724000 | Front_Seat_Heat_Cool_Switches_LS | 1 | 6 |
| 2154962944 | 0x80722000 | Front_Seat_Heat_Cool_Control_LS | 4 | 24 |
| 2156232704 | 0x80858000 | Alarm_Clock_Status_LS | 4 | 17 |
| 2154987520 | 0x80728000 | Hood_Status_LS | 1 | 4 |
| 2154840064 | 0x80704000 | Compass_Status_LS | 4 | 8 |
| 2154676224 | 0x806dc000 | Compass_Request_LS | 1 | 4 |
| 2154643456 | 0x806d4000 | Auxiliary_Heater_Status_LS | 3 | 5 |
| 2154905600 | 0x80714000 | Driver_Identifier_LS | 1 | 2 |
| 2154954752 | 0x80720000 | High_Volt_Climate_Pwr_Status_LS | 5 | 7 |
| 2153381888 | 0x805a0000 | Control_Power_Liftgate_LS | 4 | 14 |
| 2149752832 | 0x8022a000 | Chassis_Information_LS | 8 | 35 |
| 2151514112 | 0x803d8000 | Reset_OilLife_Request_LS | 1 | 1 |
| 2158903296 | 0x80ae4000 | ODIDynDataMultiRequest_AuxIP_LS | 8 | 13 |
| 2158911488 | 0x80ae6000 | ODIDynDataMultiReq_CntrStack_LS | 8 | 13 |
| 2158919680 | 0x80ae8000 | ODIDynDataMultiRequest_IPC_LS | 8 | 13 |
| 2151825408 | 0x80424000 | Outside_Air_Temperature_LS | 3 | 7 |
| 2151153664 | 0x80380000 | Rear_Window_Defog_Status_LS | 1 | 1 |
| 2151170048 | 0x80384000 | Trailer_Status_LS | 2 | 14 |
| 2151841792 | 0x80428000 | Wipe_Wash_Status_LS | 1 | 5 |
| 2154995712 | 0x8072a000 | Air_Conditioning_Comp_Type_LS | 1 | 2 |
| 2154094592 | 0x8064e000 | Adjustable_Pedal_Motion_Inh_LS | 8 | 51 |
| 2149711872 | 0x80220000 | ACC_YawRate_Information_LS | 8 | 20 |
| 2153979904 | 0x80632000 | BulbOutage_LS | 2 | 16 |
| 2150154240 | 0x8028c000 | Passive_Entry_Reply_LS | 8 | 2 |
| 2155003904 | 0x8072c000 | Side_Blind_Zone_Alert_Status | 2 | 6 |
| 2150817792 | 0x8032e000 | Airbag_Impact_Data_5 | 3 | 3 |
| 2150227968 | 0x8029e000 | Phone_Speech_Rec_Status_LS | 1 | 1 |
| 2162982912 | 0x80ec8000 | VIN_Digits_10_to_17 | 8 | 1 |
| 2162966528 | 0x80ec4000 | VIN_Digits_2_to_9 | 8 | 1 |
| 2151497728 | 0x803d4000 | Tire_Pressure_Sensors_LS | 6 | 16 |
| 2151219200 | 0x80390000 | Remote_Start_Status | 1 | 2 |
| 2153775104 | 0x80600000 | DTC_Triggered | 7 | 21 |
| 2151235584 | 0x80394000 | Vehicle_Theft_Notification_Stat | 5 | 16 |
| 2150809600 | 0x8032c000 | Airbag_Impact_Data_4 | 8 | 12 |
| 2150793216 | 0x80328000 | Airbag_Impact_Data_2 | 8 | 12 |
| 2150801408 | 0x8032a000 | Airbag_Impact_Data_3 | 8 | 12 |
| 2150785024 | 0x80326000 | Airbag_Impact_Data_1 | 8 | 11 |
| 2151202816 | 0x8038c000 | Rear_Window_Defog_Inhibit | 5 | 11 |
| 2150825984 | 0x80330000 | Airbag_Indications | 6 | 25 |
| 2151759872 | 0x80414000 | Door_Lock_Command | 4 | 14 |
| 2149974016 | 0x80260000 | Content_Theft_Sensor_Status | 3 | 17 |
| 2151907328 | 0x80438000 | Steering_Wheel_Control_Switches | 1 | 2 |
| 2150219776 | 0x8029c000 | Voice_Recognition_Status | 1 | 2 |
| 2152685568 | 0x804f6000 | Radiomarks_Response | 8 | 4 |
| 2151874560 | 0x80430000 | Vehicle_Theft_Notify_Reset_Req | 8 | 6 |
| 2150268928 | 0x802a8000 | GPS_Date_and_Time_LS | 6 | 12 |
| 2150137856 | 0x80288000 | RFA_Status_LS | 3 | 10 |
| 2151677952 | 0x80400000 | Chime_Command | 5 | 11 |
| 2150776832 | 0x80324000 | Airbag_Status | 6 | 10 |
| 2150760448 | 0x80320000 | Airbag_Impact_Data | 8 | 28 |
| 2155872256 | 0x80800000 | Fuel_Information | 6 | 14 |
| 2156175360 | 0x8084a000 | Display_Measurement_System_LS | 1 | 3 |
| 2149859328 | 0x80244000 | System_Power_Mode_Backup_LS | 1 | 4 |
| 2158854144 | 0x80ad8000 | ODIAction_IPC_LS | 8 | 6 |
| 2158837760 | 0x80ad4000 | ODIAction_AuxIP_LS | 8 | 6 |
| 2159091712 | 0x80b12000 | ODI_IPC_2_TEL_LS | 8 | 1 |
| 2154561536 | 0x806c0000 | Vehicle_Odo_LS | 5 | 3 |
| 2149908480 | 0x80250000 | Brake_Pedal_Status_LS | 2 | 7 |
| 2151268352 | 0x8039c000 | Column_Lock_Status | 1 | 1 |
| 2150604800 | 0x802fa000 | Right_Rear_Door_Status | 1 | 1 |
| 2150588416 | 0x802f6000 | Passenger_Door_Status_LS | 1 | 1 |
| 2150596608 | 0x802f8000 | Left_Rear_Door_Status | 1 | 1 |
| 2155036672 | 0x80734000 | Climate_Control_General_Status | 6 | 7 |
| 2150424576 | 0x802ce000 | Engine_Information_3_LS | 8 | 21 |
| 2150416384 | 0x802cc000 | Engine_Information_2_LS | 8 | 26 |
| 2150408192 | 0x802ca000 | Engine_Information_1_LS | 8 | 27 |
| 2155954176 | 0x80814000 | Climate_Control_Basic_Status_LS | 4 | 8 |
| 2153971712 | 0x80630000 | Driver_Door_Status | 1 | 5 |
| 2149875712 | 0x80248000 | Battery_Voltage | 7 | 17 |
| 2151186432 | 0x80388000 | Auto_High_Beam_Status | 1 | 3 |
| 2149629952 | 0x8020c000 | Lighting_Status_LS | 5 | 29 |
| 2149646336 | 0x80210000 | Vehicle_Speed_Information | 8 | 16 |
| 2154053632 | 0x80644000 | Dimming_Information_LS | 3 | 5 |
| 2149851136 | 0x80242000 | System_Power_Mode_LS | 1 | 4 |
| 2159124480 | 0x80b1a000 | ODI_AuxIP_2_TEL_LS | 8 | 1 |
| 2151530496 | 0x803dc000 | TPM_Display_Commands | 6 | 20 |

## gm_global_a_object — GM Global A platform [B]

- Make: gm; Object/ADAS bus
- Messages: 60; signals: 520
- Evidence: opendbc/opendbc/dbc/gm_global_a_object.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 3221225472 | 0xc0000000 | VECTOR__INDEPENDENT_SIG_MSG | 0 | 2 |
| 161 | 0xa1 | ASCMTimeStatus | 7 | 2 |
| 774 | 0x306 | ASCMSteeringStatus | 8 | 4 |
| 784 | 0x310 | ASCMHeadlight | 2 | 2 |
| 776 | 0x308 | ASCMAccSpeedStatus | 7 | 7 |
| 1120 | 0x460 | F_LRR_Obj_Header | 8 | 30 |
| 1134 | 0x46e | LRRObject14 | 8 | 6 |
| 1132 | 0x46c | LRRObject12 | 8 | 6 |
| 1131 | 0x46b | LRRObject11 | 8 | 6 |
| 1130 | 0x46a | LRRObject10 | 8 | 6 |
| 1129 | 0x469 | LRRObject09 | 8 | 6 |
| 1128 | 0x468 | LRRObject08 | 8 | 6 |
| 1127 | 0x467 | LRRObject07 | 8 | 6 |
| 1126 | 0x466 | LRRObject06 | 8 | 6 |
| 1125 | 0x465 | LRRObject05 | 8 | 6 |
| 1124 | 0x464 | LRRObject04 | 8 | 6 |
| 1123 | 0x463 | LRRObject03 | 8 | 6 |
| 1140 | 0x474 | LRRObject20 | 8 | 6 |
| 1139 | 0x473 | LRRObject19 | 8 | 6 |
| 1138 | 0x472 | LRRObject18 | 8 | 6 |
| 1137 | 0x471 | LRRObject17 | 8 | 6 |
| 1136 | 0x470 | LRRObject16 | 8 | 6 |
| 1135 | 0x46f | LRRObject15 | 8 | 6 |
| 1133 | 0x46d | LRRObject13 | 8 | 6 |
| 1122 | 0x462 | LRRObject02 | 8 | 6 |
| 1121 | 0x461 | LRRObject01 | 8 | 6 |
| 1094 | 0x446 | F_Vision_Obj_Track_12 | 8 | 12 |
| 1093 | 0x445 | F_Vision_Obj_Track_11 | 8 | 12 |
| 1100 | 0x44c | F_Vision_Obj_Track_12_B | 8 | 8 |
| 1099 | 0x44b | F_Vision_Obj_Track_11_B | 8 | 8 |
| 1098 | 0x44a | F_Vision_Obj_Track_10_B | 8 | 8 |
| 1097 | 0x449 | F_Vision_Obj_Track_9_B | 8 | 8 |
| 1096 | 0x448 | F_Vision_Obj_Track_8_B | 8 | 8 |
| 1095 | 0x447 | F_Vision_Obj_Track_7_B | 8 | 8 |
| 1068 | 0x42c | F_Vision_Obj_Track_6_B | 8 | 8 |
| 1067 | 0x42b | F_Vision_Obj_Track_5_B | 8 | 8 |
| 1066 | 0x42a | F_Vision_Obj_Track_4_B | 8 | 8 |
| 1065 | 0x429 | F_Vision_Obj_Track_3_B | 8 | 8 |
| 1064 | 0x428 | F_Vision_Obj_Track_2_B | 8 | 8 |
| 1063 | 0x427 | F_Vision_Obj_Track_1_B | 8 | 8 |
| 1088 | 0x440 | F_Vision_Obj_Header_2 | 8 | 11 |
| 854 | 0x356 | F_Vision_Environment_7 | 3 | 7 |
| 853 | 0x355 | F_Vision_Environment_6 | 8 | 11 |
| 852 | 0x354 | F_Vision_Environment_5 | 8 | 11 |
| 309 | 0x135 | LHT_CameraObjConfirmation_FO | 1 | 2 |
| 848 | 0x350 | F_Vision_Environment | 8 | 14 |
| 849 | 0x351 | F_Vision_Environment_2 | 8 | 11 |
| 1056 | 0x420 | F_Vision_Obj_Header | 6 | 12 |
| 1057 | 0x421 | F_Vision_Obj_Track_1 | 8 | 12 |
| 1058 | 0x422 | F_Vision_Obj_Track_2 | 8 | 12 |
| 1059 | 0x423 | F_Vision_Obj_Track_3 | 8 | 12 |
| 1060 | 0x424 | F_Vision_Obj_Track_4 | 8 | 12 |
| 1061 | 0x425 | F_Vision_Obj_Track_5 | 8 | 12 |
| 1062 | 0x426 | F_Vision_Obj_Track_6 | 8 | 12 |
| 1089 | 0x441 | F_Vision_Obj_Track_7 | 8 | 12 |
| 1090 | 0x442 | F_Vision_Obj_Track_8 | 8 | 12 |
| 1091 | 0x443 | F_Vision_Obj_Track_9 | 8 | 12 |
| 1092 | 0x444 | F_Vision_Obj_Track_10 | 8 | 12 |
| 851 | 0x353 | F_Vision_Environment_4 | 8 | 18 |
| 850 | 0x352 | F_Vision_Environment_3 | 8 | 16 |

## gm_global_a_powertrain_expansion — GM Global A platform [B]

- Make: gm; Powertrain expansion
- Messages: 2; signals: 9
- Evidence: opendbc/opendbc/dbc/gm_global_a_powertrain_expansion.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 470 | 0x1d6 | APM_Stats | 7 | 7 |
| 468 | 0x1d4 | APM_Command | 2 | 2 |

## FORD_CADS — Ford CADS [B]

- Make: ford; Comma AI Ford ADAS DBC
- Messages: 81; signals: 811
- Evidence: opendbc/opendbc/dbc/FORD_CADS.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 1073741824 | 0x40000000 | VECTOR__INDEPENDENT_SIG_MSG | 0 | 27 |
| 34 | 0x22 | Active_Fault_Latched_2 | 8 | 5 |
| 33 | 0x21 | Active_Fault_Latched_1 | 8 | 64 |
| 500 | 0x1f4 | XCP_MRR_DAQ_RESP | 8 | 8 |
| 499 | 0x1f3 | XCP_MRR_DTO_RESP | 8 | 8 |
| 497 | 0x1f1 | XCP_MRR_CTO_RESP | 8 | 8 |
| 1900 | 0x76c | Ford_Diag_Resp_Phys | 8 | 1 |
| 261 | 0x105 | MRR_Status_SerialNumber | 8 | 2 |
| 264 | 0x108 | MRR_Status_SwVersion | 8 | 6 |
| 373 | 0x175 | MRR_Header_SensorPosition | 8 | 4 |
| 372 | 0x174 | MRR_Header_SensorCoverage | 8 | 3 |
| 371 | 0x173 | MRR_Header_AlignmentState | 8 | 5 |
| 369 | 0x171 | MRR_Header_Timestamps | 8 | 2 |
| 368 | 0x170 | MRR_Header_InformationDetections | 8 | 5 |
| 265 | 0x109 | MRR_Status_Temp_Volt | 8 | 8 |
| 291 | 0x123 | MRR_Detection_004 | 8 | 10 |
| 351 | 0x15f | MRR_Detection_064 | 8 | 10 |
| 350 | 0x15e | MRR_Detection_063 | 8 | 10 |
| 349 | 0x15d | MRR_Detection_062 | 8 | 10 |
| 348 | 0x15c | MRR_Detection_061 | 8 | 10 |
| 347 | 0x15b | MRR_Detection_060 | 8 | 10 |
| 346 | 0x15a | MRR_Detection_059 | 8 | 10 |
| 345 | 0x159 | MRR_Detection_058 | 8 | 10 |
| 344 | 0x158 | MRR_Detection_057 | 8 | 10 |
| 343 | 0x157 | MRR_Detection_056 | 8 | 10 |
| 342 | 0x156 | MRR_Detection_055 | 8 | 10 |
| 335 | 0x14f | MRR_Detection_048 | 8 | 10 |
| 334 | 0x14e | MRR_Detection_047 | 8 | 10 |
| 333 | 0x14d | MRR_Detection_046 | 8 | 10 |
| 332 | 0x14c | MRR_Detection_045 | 8 | 10 |
| 331 | 0x14b | MRR_Detection_044 | 8 | 10 |
| 330 | 0x14a | MRR_Detection_043 | 8 | 10 |
| 329 | 0x149 | MRR_Detection_042 | 8 | 10 |
| 328 | 0x148 | MRR_Detection_041 | 8 | 10 |
| 327 | 0x147 | MRR_Detection_040 | 8 | 10 |
| 325 | 0x145 | MRR_Detection_038 | 8 | 10 |
| 324 | 0x144 | MRR_Detection_037 | 8 | 10 |
| 323 | 0x143 | MRR_Detection_036 | 8 | 10 |
| 322 | 0x142 | MRR_Detection_035 | 8 | 10 |
| 321 | 0x141 | MRR_Detection_034 | 8 | 10 |
| 320 | 0x140 | MRR_Detection_033 | 8 | 10 |
| 319 | 0x13f | MRR_Detection_032 | 8 | 10 |
| 318 | 0x13e | MRR_Detection_031 | 8 | 10 |
| 317 | 0x13d | MRR_Detection_030 | 8 | 10 |
| 316 | 0x13c | MRR_Detection_029 | 8 | 10 |
| 314 | 0x13a | MRR_Detection_027 | 8 | 10 |
| 313 | 0x139 | MRR_Detection_026 | 8 | 10 |
| 312 | 0x138 | MRR_Detection_025 | 8 | 10 |
| 311 | 0x137 | MRR_Detection_024 | 8 | 10 |
| 310 | 0x136 | MRR_Detection_023 | 8 | 10 |
| 309 | 0x135 | MRR_Detection_022 | 8 | 10 |
| 308 | 0x134 | MRR_Detection_021 | 8 | 10 |
| 307 | 0x133 | MRR_Detection_020 | 8 | 10 |
| 306 | 0x132 | MRR_Detection_019 | 8 | 10 |
| 305 | 0x131 | MRR_Detection_018 | 8 | 10 |
| 341 | 0x155 | MRR_Detection_054 | 8 | 10 |
| 340 | 0x154 | MRR_Detection_053 | 8 | 10 |
| 339 | 0x153 | MRR_Detection_052 | 8 | 10 |
| 338 | 0x152 | MRR_Detection_051 | 8 | 10 |
| 337 | 0x151 | MRR_Detection_050 | 8 | 10 |
| 336 | 0x150 | MRR_Detection_049 | 8 | 10 |
| 326 | 0x146 | MRR_Detection_039 | 8 | 10 |
| 315 | 0x13b | MRR_Detection_028 | 8 | 10 |
| 304 | 0x130 | MRR_Detection_017 | 8 | 10 |
| 303 | 0x12f | MRR_Detection_016 | 8 | 10 |
| 302 | 0x12e | MRR_Detection_015 | 8 | 10 |
| 301 | 0x12d | MRR_Detection_014 | 8 | 10 |
| 300 | 0x12c | MRR_Detection_013 | 8 | 10 |
| 299 | 0x12b | MRR_Detection_012 | 8 | 10 |
| 298 | 0x12a | MRR_Detection_011 | 8 | 10 |
| 297 | 0x129 | MRR_Detection_010 | 8 | 10 |
| 296 | 0x128 | MRR_Detection_009 | 8 | 10 |
| 295 | 0x127 | MRR_Detection_008 | 8 | 10 |
| 294 | 0x126 | MRR_Detection_007 | 8 | 10 |
| 293 | 0x125 | MRR_Detection_006 | 8 | 10 |
| 292 | 0x124 | MRR_Detection_005 | 8 | 10 |
| 290 | 0x122 | MRR_Detection_003 | 8 | 10 |
| 289 | 0x121 | MRR_Detection_002 | 8 | 10 |
| 256 | 0x100 | MRR_Status_CANVersion | 8 | 3 |
| 257 | 0x101 | MRR_Status_Radar | 8 | 12 |
| 288 | 0x120 | MRR_Detection_001 | 8 | 10 |

## FORD_CADS_64 — Ford CADS [B]

- Make: ford; Comma AI Ford ADAS DBC, 64-bit variant
- Messages: 81; signals: 1881
- Evidence: opendbc/opendbc/dbc/FORD_CADS_64.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 1073741824 | 0x40000000 | VECTOR__INDEPENDENT_SIG_MSG | 0 | 27 |
| 34 | 0x22 | Active_Fault_Latched_2 | 8 | 5 |
| 33 | 0x21 | Active_Fault_Latched_1 | 8 | 64 |
| 500 | 0x1f4 | XCP_MRR_DAQ_RESP | 8 | 8 |
| 499 | 0x1f3 | XCP_MRR_DTO_RESP | 8 | 8 |
| 497 | 0x1f1 | XCP_MRR_CTO_RESP | 8 | 8 |
| 1900 | 0x76c | Ford_Diag_Resp_Phys | 8 | 1 |
| 261 | 0x105 | MRR_Status_SerialNumber | 8 | 2 |
| 264 | 0x108 | MRR_Status_SwVersion | 8 | 6 |
| 373 | 0x175 | MRR_Header_SensorPosition | 8 | 4 |
| 372 | 0x174 | MRR_Header_SensorCoverage | 8 | 3 |
| 371 | 0x173 | MRR_Header_AlignmentState | 8 | 5 |
| 369 | 0x171 | MRR_Header_Timestamps | 8 | 2 |
| 368 | 0x170 | MRR_Header_InformationDetections | 8 | 5 |
| 265 | 0x109 | MRR_Status_Temp_Volt | 8 | 8 |
| 291 | 0x123 | MRR_Detection_004 | 64 | 60 |
| 351 | 0x15f | MRR_Detection_064 | 8 | 10 |
| 350 | 0x15e | MRR_Detection_063 | 8 | 10 |
| 349 | 0x15d | MRR_Detection_062 | 8 | 10 |
| 348 | 0x15c | MRR_Detection_061 | 8 | 10 |
| 347 | 0x15b | MRR_Detection_060 | 8 | 10 |
| 346 | 0x15a | MRR_Detection_059 | 8 | 10 |
| 345 | 0x159 | MRR_Detection_058 | 8 | 10 |
| 344 | 0x158 | MRR_Detection_057 | 8 | 10 |
| 343 | 0x157 | MRR_Detection_056 | 8 | 10 |
| 342 | 0x156 | MRR_Detection_055 | 8 | 10 |
| 335 | 0x14f | MRR_Detection_048 | 8 | 10 |
| 334 | 0x14e | MRR_Detection_047 | 8 | 10 |
| 333 | 0x14d | MRR_Detection_046 | 8 | 10 |
| 332 | 0x14c | MRR_Detection_045 | 8 | 10 |
| 331 | 0x14b | MRR_Detection_044 | 8 | 10 |
| 330 | 0x14a | MRR_Detection_043 | 8 | 10 |
| 329 | 0x149 | MRR_Detection_042 | 8 | 10 |
| 328 | 0x148 | MRR_Detection_041 | 8 | 10 |
| 327 | 0x147 | MRR_Detection_040 | 8 | 10 |
| 325 | 0x145 | MRR_Detection_038 | 8 | 10 |
| 324 | 0x144 | MRR_Detection_037 | 8 | 10 |
| 323 | 0x143 | MRR_Detection_036 | 8 | 10 |
| 322 | 0x142 | MRR_Detection_035 | 8 | 10 |
| 321 | 0x141 | MRR_Detection_034 | 8 | 10 |
| 320 | 0x140 | MRR_Detection_033 | 8 | 10 |
| 319 | 0x13f | MRR_Detection_032 | 8 | 10 |
| 318 | 0x13e | MRR_Detection_031 | 8 | 10 |
| 317 | 0x13d | MRR_Detection_030 | 8 | 10 |
| 316 | 0x13c | MRR_Detection_029 | 8 | 10 |
| 314 | 0x13a | MRR_Detection_027 | 8 | 10 |
| 313 | 0x139 | MRR_Detection_026 | 8 | 10 |
| 312 | 0x138 | MRR_Detection_025 | 8 | 10 |
| 311 | 0x137 | MRR_Detection_024 | 8 | 10 |
| 310 | 0x136 | MRR_Detection_023 | 8 | 10 |
| 309 | 0x135 | MRR_Detection_022 | 24 | 30 |
| 308 | 0x134 | MRR_Detection_021 | 64 | 60 |
| 307 | 0x133 | MRR_Detection_020 | 64 | 60 |
| 306 | 0x132 | MRR_Detection_019 | 64 | 60 |
| 305 | 0x131 | MRR_Detection_018 | 64 | 60 |
| 341 | 0x155 | MRR_Detection_054 | 8 | 10 |
| 340 | 0x154 | MRR_Detection_053 | 8 | 10 |
| 339 | 0x153 | MRR_Detection_052 | 8 | 10 |
| 338 | 0x152 | MRR_Detection_051 | 8 | 10 |
| 337 | 0x151 | MRR_Detection_050 | 8 | 10 |
| 336 | 0x150 | MRR_Detection_049 | 8 | 10 |
| 326 | 0x146 | MRR_Detection_039 | 8 | 10 |
| 315 | 0x13b | MRR_Detection_028 | 8 | 10 |
| 304 | 0x130 | MRR_Detection_017 | 64 | 60 |
| 303 | 0x12f | MRR_Detection_016 | 64 | 60 |
| 302 | 0x12e | MRR_Detection_015 | 64 | 60 |
| 301 | 0x12d | MRR_Detection_014 | 64 | 60 |
| 300 | 0x12c | MRR_Detection_013 | 64 | 60 |
| 299 | 0x12b | MRR_Detection_012 | 64 | 60 |
| 298 | 0x12a | MRR_Detection_011 | 64 | 60 |
| 297 | 0x129 | MRR_Detection_010 | 64 | 60 |
| 296 | 0x128 | MRR_Detection_009 | 64 | 60 |
| 295 | 0x127 | MRR_Detection_008 | 64 | 60 |
| 294 | 0x126 | MRR_Detection_007 | 64 | 60 |
| 293 | 0x125 | MRR_Detection_006 | 64 | 60 |
| 292 | 0x124 | MRR_Detection_005 | 64 | 60 |
| 290 | 0x122 | MRR_Detection_003 | 64 | 60 |
| 289 | 0x121 | MRR_Detection_002 | 64 | 60 |
| 256 | 0x100 | MRR_Status_CANVersion | 8 | 3 |
| 257 | 0x101 | MRR_Status_Radar | 8 | 12 |
| 288 | 0x120 | MRR_Detection_001 | 64 | 60 |

## ford_cgea1_2_bodycan_2011 — Ford CGEA 1.2 [B]

- Make: ford; Body CAN, 2011 platform
- Messages: 102; signals: 829
- Evidence: opendbc/opendbc/dbc/ford_cgea1_2_bodycan_2011.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 58 | 0x3a | BCM_m_FrP01 | 8 | 18 |
| 64 | 0x40 | BCM_m_FrP02 | 8 | 25 |
| 131 | 0x83 | MS_Steering_Data | 8 | 30 |
| 257 | 0x101 | Driver_Seat_Information | 8 | 3 |
| 260 | 0x104 | Driver_Seat_Information_2 | 8 | 4 |
| 269 | 0x10d | IdleShutdown_Legacy | 8 | 1 |
| 272 | 0x110 | Keyfob_Pad_Stat | 8 | 8 |
| 275 | 0x113 | Power_Liftgate_Mode_StatM | 8 | 2 |
| 276 | 0x114 | Running_Board_CmdM | 8 | 1 |
| 277 | 0x115 | Running_Board_StatM | 8 | 1 |
| 288 | 0x120 | ClmtCtrlSeat_SetCmdlegacy1 | 8 | 1 |
| 289 | 0x121 | ClmtCtrlSeat_SetStat_DvrM | 8 | 1 |
| 290 | 0x122 | ClmtCtrlSeat_SetCmdlegacy2 | 8 | 1 |
| 291 | 0x123 | ClmtCtrlSeat_SetStat_PsgrM | 8 | 1 |
| 292 | 0x124 | ClmtCtrlSeatSet_Cmd_v2_MS | 8 | 2 |
| 293 | 0x125 | ClmtCtrlSeatSet_Stat_v2 | 8 | 2 |
| 304 | 0x130 | Mirror_Manual_Override_M | 8 | 1 |
| 305 | 0x131 | Memory_Sw_StatM | 8 | 6 |
| 306 | 0x132 | Driver_Lock_Sw_StatM | 8 | 4 |
| 309 | 0x135 | Memory_Cancel_Cmd_M | 8 | 1 |
| 310 | 0x136 | Driver_Door_Lock_CmdM | 8 | 2 |
| 311 | 0x137 | Pass_Mirror_Sw_StatM | 8 | 2 |
| 313 | 0x139 | RPwrSlideDr_Unlock_RqstM | 8 | 1 |
| 320 | 0x140 | LPwrSlideDr_Unlock_RqstM | 8 | 1 |
| 321 | 0x141 | Passive_Entry_Ctrl_Data | 8 | 10 |
| 322 | 0x142 | Passive_Entry_Target_Data | 8 | 8 |
| 577 | 0x241 | BCM_m_FrP28 | 8 | 8 |
| 736 | 0x2e0 | FCIM_Button_Press | 8 | 3 |
| 806 | 0x326 | Compressor_Req | 8 | 4 |
| 842 | 0x34a | MassageSeat_Data1 | 8 | 5 |
| 843 | 0x34b | MassageSeat_Data2 | 8 | 5 |
| 844 | 0x34c | MassageSeat_Stat1 | 8 | 6 |
| 845 | 0x34d | MassageSeat_Stat2 | 8 | 6 |
| 846 | 0x34e | MassageSeat_Req_MS | 8 | 7 |
| 849 | 0x351 | MassageSeat_Data3 | 8 | 4 |
| 850 | 0x352 | MassageSeat_Data4 | 8 | 4 |
| 853 | 0x355 | EFP_CC_Status_MS | 8 | 16 |
| 854 | 0x356 | EFP_CC_Seat_Req_Stat_MS | 8 | 9 |
| 855 | 0x357 | RCCM_CC_Status | 8 | 16 |
| 856 | 0x358 | RCCM_CC_Seat_Status | 8 | 14 |
| 857 | 0x359 | RCCM_CC_MBP_Press_Stat | 8 | 8 |
| 859 | 0x35b | MFD_CC_Status_MS | 8 | 1 |
| 860 | 0x35c | EFP_CC_Info_Status_MS | 8 | 30 |
| 861 | 0x35d | HSWheel_CC_Info_Stat | 8 | 1 |
| 862 | 0x35e | Climate_Control_Data_2 | 8 | 4 |
| 900 | 0x384 | Vehicle_Access_RqstM | 8 | 17 |
| 901 | 0x385 | Vehicle_Lock_Status | 8 | 14 |
| 902 | 0x386 | Remote_Start | 8 | 1 |
| 903 | 0x387 | CC_FCIM_Update | 8 | 43 |
| 904 | 0x388 | CC_NavChassis_Info_Status | 8 | 27 |
| 920 | 0x398 | FCIM_CC_Status | 8 | 34 |
| 921 | 0x399 | Nav_CC_Status | 8 | 6 |
| 922 | 0x39a | VoiceRec_CC_Request | 8 | 20 |
| 928 | 0x3a0 | Ignition_Switch_PositionM | 8 | 10 |
| 934 | 0x3a6 | Side_Detect_L_StatusM | 8 | 8 |
| 935 | 0x3a7 | Side_Detect_R_StatusM | 8 | 8 |
| 944 | 0x3b0 | Body_Information_6_MS | 8 | 4 |
| 945 | 0x3b1 | Ajar_Stat | 8 | 8 |
| 946 | 0x3b2 | Body_Information_5_MS | 8 | 14 |
| 947 | 0x3b3 | BodyInformation_3_MS | 8 | 20 |
| 950 | 0x3b6 | RKE_Packet | 8 | 5 |
| 951 | 0x3b7 | TPM_Frame | 8 | 5 |
| 952 | 0x3b8 | RKE_TPM_Info | 8 | 6 |
| 953 | 0x3b9 | RKE_Info | 8 | 5 |
| 954 | 0x3ba | Tire_Pressure_Info | 8 | 3 |
| 956 | 0x3bc | Body_Information_7_MS | 8 | 7 |
| 958 | 0x3be | Rear_FoglampStat | 8 | 1 |
| 963 | 0x3c3 | BCM_to_MS_Body | 8 | 32 |
| 964 | 0x3c4 | BodyInformation_2_MS | 8 | 30 |
| 966 | 0x3c6 | Delay_AccyM_for_P473 | 8 | 1 |
| 967 | 0x3c7 | CMPS_FDM_Info_StatusMS | 8 | 10 |
| 968 | 0x3c8 | EATC_FDM_Info_Status | 8 | 17 |
| 969 | 0x3c9 | Aux_Body_Ctrl_Mod_Status | 8 | 4 |
| 976 | 0x3d0 | Veh_Characteristic_Set_2 | 8 | 12 |
| 977 | 0x3d1 | ClmtCtrlSeat_SetCmd_LRPM | 8 | 1 |
| 978 | 0x3d2 | ClmtCtrlSeat_SetStat_LRPM | 8 | 1 |
| 979 | 0x3d3 | ClmtCtrlSeat_SetCmd_RRPM | 8 | 1 |
| 980 | 0x3d4 | ClmtCtrlSeat_SetStat_RRPM | 8 | 1 |
| 981 | 0x3d5 | Rear_HVAC_Control_Status | 8 | 8 |
| 982 | 0x3d6 | Rear_HVAC_Control_Update | 8 | 7 |
| 986 | 0x3da | Personality_APIM_Data3_MS | 8 | 6 |
| 987 | 0x3db | RHVAC_Data | 8 | 1 |
| 992 | 0x3e0 | Personality_Data_MS | 8 | 11 |
| 993 | 0x3e1 | Personality_DSM_Data | 8 | 6 |
| 994 | 0x3e2 | Personality_Data_MS_2 | 8 | 13 |
| 996 | 0x3e4 | Personality_HCMB_Data | 8 | 3 |
| 999 | 0x3e7 | Personality_HVAC_Data | 8 | 5 |
| 1000 | 0x3e8 | ACM_Status_Message | 8 | 1 |
| 1001 | 0x3e9 | Personality_RFA_Data | 8 | 3 |
| 1005 | 0x3ed | Personality_RHVAC_Data | 8 | 3 |
| 1006 | 0x3ee | Nav_HMI_Status | 8 | 7 |
| 1023 | 0x3ff | Reserve_3FF_MKX_Audio | 8 | 1 |
| 1034 | 0x40a | GGCC_Config_Mgmt_ID_1 | 8 | 1 |
| 1050 | 0x41a | Climate_Control_Data | 8 | 11 |
| 1059 | 0x423 | Engine_Data_MS | 8 | 12 |
| 1061 | 0x425 | Engine_Data_2_MS | 8 | 13 |
| 1062 | 0x426 | ACM_NAV_WHEEL_INFO | 8 | 19 |
| 1068 | 0x42c | Battery_Mgmt_2_MS | 8 | 6 |
| 1125 | 0x465 | GPS_Data_Nav_1 | 8 | 8 |
| 1126 | 0x466 | GPS_Data_Nav_2 | 8 | 10 |
| 1127 | 0x467 | GPS_Data_Nav_3 | 8 | 7 |
| 1144 | 0x478 | GPS_Data_Nav_4 | 8 | 3 |

## ford_cgea1_2_ptcan_2011 — Ford CGEA 1.2 [B]

- Make: ford; Powertrain CAN, 2011 platform
- Messages: 143; signals: 1164
- Evidence: opendbc/opendbc/dbc/ford_cgea1_2_ptcan_2011.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 65 | 0x41 | Global_PATS_Control_Info | 8 | 2 |
| 66 | 0x42 | Global_PATS_Control_Info2 | 8 | 2 |
| 71 | 0x47 | Global_PATS_Target_Info | 8 | 3 |
| 72 | 0x48 | Global_PATS_Target_Info_2 | 8 | 3 |
| 73 | 0x49 | Global_PATS_SubTarget_FoE | 8 | 2 |
| 74 | 0x4a | VehEmergencyData1 | 8 | 14 |
| 75 | 0x4b | VehEmergencyData2 | 8 | 11 |
| 116 | 0x74 | BrakeSnData_2_CG1 | 8 | 8 |
| 117 | 0x75 | BrakeSnData_3_CG1 | 8 | 7 |
| 124 | 0x7c | BrakeSnData_4_CG1 | 8 | 6 |
| 129 | 0x81 | Steering_Wheel_Data2 | 8 | 10 |
| 130 | 0x82 | EPAS_INFO | 8 | 10 |
| 131 | 0x83 | Steering_Data | 8 | 20 |
| 132 | 0x84 | Steering_Wheel_Data_CG1 | 8 | 5 |
| 145 | 0x91 | Yaw_Data | 8 | 3 |
| 146 | 0x92 | Accel_Data | 8 | 6 |
| 258 | 0x102 | Cluster_Legacy | 8 | 7 |
| 259 | 0x103 | Body_MsgCntr_Stat_CG1 | 8 | 7 |
| 264 | 0x108 | Side_Detect_CmdM | 8 | 2 |
| 266 | 0x10a | ParkAid_Audible_Warn_CmdM | 8 | 3 |
| 267 | 0x10b | ParkAid_Audible_Warn_Stat | 8 | 8 |
| 292 | 0x124 | ClmtCtrlSeatSet_Cmd_v2 | 8 | 2 |
| 293 | 0x125 | ClmtCtrlSeatSetStat_v2_HS | 8 | 2 |
| 336 | 0x150 | TransData_1_CG1 | 8 | 4 |
| 337 | 0x151 | EngineData_1_CG1 | 8 | 7 |
| 338 | 0x152 | TransData_2_CG1 | 8 | 4 |
| 339 | 0x153 | EngineData_2_CG1 | 8 | 4 |
| 340 | 0x154 | EngineData_3_CG1 | 8 | 6 |
| 341 | 0x155 | EngineData_11_CG1 | 8 | 15 |
| 342 | 0x156 | Engine_Data_6 | 8 | 9 |
| 343 | 0x157 | EngineData_13_CG1 | 8 | 8 |
| 344 | 0x158 | EngineData_14 | 8 | 3 |
| 345 | 0x159 | Engine_Data_7_CG1 | 8 | 15 |
| 346 | 0x15a | EngineData_4_CG1 | 8 | 6 |
| 348 | 0x15c | EngineData_16_CG1 | 8 | 9 |
| 349 | 0x15d | EngineData_17_CG1 | 8 | 8 |
| 350 | 0x15e | EngineData_18_CG1 | 8 | 5 |
| 351 | 0x15f | EngineData_19 | 8 | 5 |
| 352 | 0x160 | TransData_3_CG1 | 8 | 4 |
| 353 | 0x161 | Engine_Data_8 | 8 | 4 |
| 354 | 0x162 | CGEA_Urea_Strategy_CG1 | 8 | 5 |
| 355 | 0x163 | EngineData_10 | 8 | 8 |
| 357 | 0x165 | EngBrakeData | 8 | 12 |
| 389 | 0x185 | ACCDATA_CG1 | 8 | 13 |
| 392 | 0x188 | HeadUpDisplayStat | 8 | 3 |
| 393 | 0x189 | ACCDATA_2_CG1 | 8 | 17 |
| 394 | 0x18a | ACCDATA_3 | 8 | 26 |
| 512 | 0x200 | TorqueDataEngFlags | 8 | 6 |
| 513 | 0x201 | EngVehicleSpThrottle_CG1 | 8 | 9 |
| 529 | 0x211 | DesiredTorqBrk_CG1 | 8 | 20 |
| 533 | 0x215 | WheelSpeed_CG1 | 8 | 4 |
| 534 | 0x216 | WheelData | 8 | 9 |
| 557 | 0x22d | InfoCAN_22D | 8 | 1 |
| 560 | 0x230 | TransGearData | 8 | 12 |
| 561 | 0x231 | TransGearData_2 | 8 | 7 |
| 562 | 0x232 | TransGearData_3_CG1 | 8 | 8 |
| 563 | 0x233 | TransGearData_4_CG1 | 8 | 6 |
| 570 | 0x23a | Suspension_Stat | 8 | 5 |
| 571 | 0x23b | ColumnLockData | 8 | 1 |
| 576 | 0x240 | Body_Information_4_CG1 | 8 | 15 |
| 592 | 0x250 | EONV_Status | 8 | 10 |
| 597 | 0x255 | EONV_Control | 8 | 6 |
| 608 | 0x260 | Information4x4_CG1 | 8 | 15 |
| 609 | 0x261 | AWD_4x4_Data | 8 | 2 |
| 613 | 0x265 | PassengerSeatOCSInfo | 8 | 7 |
| 736 | 0x2e0 | FCIM_Button_Press_HS | 8 | 6 |
| 806 | 0x326 | Compressor_Req_HS | 8 | 4 |
| 832 | 0x340 | RCMStatusMessage | 8 | 29 |
| 842 | 0x34a | MassageSeat_Data1_HS | 8 | 5 |
| 843 | 0x34b | MassageSeat_Data2_HS | 8 | 5 |
| 844 | 0x34c | MassageSeat_Stat1_HS | 8 | 6 |
| 845 | 0x34d | MassageSeat_Stat2_HS | 8 | 6 |
| 846 | 0x34e | MassageSeat_Req | 8 | 7 |
| 848 | 0x350 | RestraintsData | 8 | 5 |
| 849 | 0x351 | MassageSeat_Data3_HS | 8 | 4 |
| 850 | 0x352 | MassageSeat_Data4_HS | 8 | 4 |
| 853 | 0x355 | EFP_CC_Status | 8 | 16 |
| 854 | 0x356 | EFP_CC_Seat_Req_Stat | 8 | 9 |
| 855 | 0x357 | RCCM_CC_Status_HS | 8 | 16 |
| 856 | 0x358 | RCCM_CC_Seat_Status_HS | 8 | 14 |
| 857 | 0x359 | RCCM_CC_MBP_Press_Stat_HS | 8 | 8 |
| 859 | 0x35b | MFD_CC_Status_HS | 8 | 9 |
| 860 | 0x35c | EFP_CC_Info_Status | 8 | 30 |
| 890 | 0x37a | Active_Noise | 8 | 3 |
| 891 | 0x37b | Active_Noise_Data | 8 | 1 |
| 906 | 0x38a | Body_Information_1 | 8 | 15 |
| 909 | 0x38d | Body_Information_6 | 8 | 25 |
| 936 | 0x3a8 | ParkAid_Data | 8 | 3 |
| 937 | 0x3a9 | ParkAid_Range_to_Target | 8 | 5 |
| 939 | 0x3ab | ParkAid_Data_CG1 | 8 | 4 |
| 942 | 0x3ae | BodyInformation_2 | 8 | 25 |
| 947 | 0x3b3 | BodyInformation_3 | 8 | 22 |
| 948 | 0x3b4 | Tire_Pressure_Status | 8 | 8 |
| 949 | 0x3b5 | Tire_Pressure_Data | 8 | 6 |
| 955 | 0x3bb | Smart_Headlamp_Stat | 8 | 3 |
| 957 | 0x3bd | Rear_FogLamp | 8 | 1 |
| 963 | 0x3c3 | BCM_to_HS_Body | 8 | 33 |
| 967 | 0x3c7 | CMPS_FDM_Info_Status | 8 | 20 |
| 970 | 0x3ca | Lane_Assist_Data1 | 8 | 3 |
| 971 | 0x3cb | Lane_Assist_Data2 | 8 | 3 |
| 972 | 0x3cc | Lane_Assist_Data3 | 8 | 3 |
| 984 | 0x3d8 | IPMA_Data | 8 | 14 |
| 986 | 0x3da | Personality_APIM_Data3 | 8 | 6 |
| 991 | 0x3df | Personality_VDM_Data | 8 | 3 |
| 992 | 0x3e0 | Personality_IPC_Data | 8 | 4 |
| 993 | 0x3e1 | Personality_Data_HS | 8 | 9 |
| 994 | 0x3e2 | Personality_APIM_Data | 8 | 10 |
| 995 | 0x3e3 | Personality_BCM_Data | 8 | 3 |
| 996 | 0x3e4 | Personality_HCMB_Data_HS | 8 | 6 |
| 997 | 0x3e5 | Personality_CCM_Data | 8 | 3 |
| 998 | 0x3e6 | Personality_SCCM_Data | 8 | 3 |
| 999 | 0x3e7 | Personality_HVAC_Data_HS | 8 | 10 |
| 1001 | 0x3e9 | Personality_RFA_Data_HS | 8 | 6 |
| 1002 | 0x3ea | Personality_APIM_Data2 | 8 | 6 |
| 1003 | 0x3eb | Personality_IPC_Data_2 | 8 | 3 |
| 1004 | 0x3ec | Personality_DSM_Data_HS | 8 | 6 |
| 1005 | 0x3ed | Personality_RHVAC_Data_HS | 8 | 6 |
| 1031 | 0x407 | Diesel_Data_Legacy_1 | 8 | 3 |
| 1034 | 0x40a | GGCC_Config_Mgmt_ID_1 | 8 | 1 |
| 1036 | 0x40c | Desired_Torq_BrkSys_Stat | 8 | 2 |
| 1043 | 0x413 | ADAPTIVE_HEADLAMP_STAT | 8 | 1 |
| 1044 | 0x414 | AccelerationData | 8 | 4 |
| 1045 | 0x415 | BrakeSysFeatures | 8 | 15 |
| 1046 | 0x416 | BrakeSysFeatures_2 | 8 | 14 |
| 1047 | 0x417 | TractionCtrlStatus_CG1 | 8 | 12 |
| 1056 | 0x420 | PowertrainData_1_CG1 | 8 | 11 |
| 1058 | 0x422 | PowertrainData_2_CG1 | 8 | 8 |
| 1064 | 0x428 | StrgWheel_PolicePkg | 8 | 4 |
| 1067 | 0x42b | Battery_Mgmt_1 | 8 | 9 |
| 1068 | 0x42c | Battery_Mgmt_2 | 8 | 15 |
| 1069 | 0x42d | Battery_Mgmt_3 | 8 | 6 |
| 1072 | 0x430 | Cluster_Information | 8 | 24 |
| 1075 | 0x433 | Cluster_Information_3_CG1 | 8 | 23 |
| 1093 | 0x445 | TrailerBrakeInfo | 8 | 10 |
| 1104 | 0x450 | SHCM_Status | 8 | 2 |
| 1107 | 0x453 | PassengerOCSSerialNum | 8 | 8 |
| 1108 | 0x454 | RCMSerialNumber | 8 | 8 |
| 1109 | 0x455 | eCall_Info | 8 | 1 |
| 1125 | 0x465 | GPS_Data_Nav_1_HS | 8 | 8 |
| 1126 | 0x466 | GPS_Data_Nav_2_HS | 8 | 10 |
| 1127 | 0x467 | GPS_Data_Nav_3_HS | 8 | 7 |
| 1152 | 0x480 | All_Terrain_Data | 8 | 3 |
| 1186 | 0x4a2 | Information_4x4_2_CG1 | 8 | 5 |

## ford_fusion_2018_adas — Ford Fusion 2018 [B]

- Make: ford; ADAS bus
- Messages: 64; signals: 256
- Evidence: opendbc/opendbc/dbc/ford_fusion_2018_adas.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 1280 | 0x500 | Object_00 | 8 | 4 |
| 1281 | 0x501 | Object_01 | 8 | 4 |
| 1282 | 0x502 | Object_02 | 8 | 4 |
| 1283 | 0x503 | Object_03 | 8 | 4 |
| 1284 | 0x504 | Object_04 | 8 | 4 |
| 1285 | 0x505 | Object_05 | 8 | 4 |
| 1286 | 0x506 | Object_06 | 8 | 4 |
| 1287 | 0x507 | Object_07 | 8 | 4 |
| 1288 | 0x508 | Object_08 | 8 | 4 |
| 1289 | 0x509 | Object_09 | 8 | 4 |
| 1290 | 0x50a | Object_10 | 8 | 4 |
| 1291 | 0x50b | Object_11 | 8 | 4 |
| 1292 | 0x50c | Object_12 | 8 | 4 |
| 1293 | 0x50d | Object_13 | 8 | 4 |
| 1294 | 0x50e | Object_14 | 8 | 4 |
| 1295 | 0x50f | Object_15 | 8 | 4 |
| 1296 | 0x510 | Object_16 | 8 | 4 |
| 1297 | 0x511 | Object_17 | 8 | 4 |
| 1298 | 0x512 | Object_18 | 8 | 4 |
| 1299 | 0x513 | Object_19 | 8 | 4 |
| 1300 | 0x514 | Object_20 | 8 | 4 |
| 1301 | 0x515 | Object_21 | 8 | 4 |
| 1302 | 0x516 | Object_22 | 8 | 4 |
| 1303 | 0x517 | Object_23 | 8 | 4 |
| 1304 | 0x518 | Object_24 | 8 | 4 |
| 1305 | 0x519 | Object_25 | 8 | 4 |
| 1306 | 0x51a | Object_26 | 8 | 4 |
| 1307 | 0x51b | Object_27 | 8 | 4 |
| 1308 | 0x51c | Object_28 | 8 | 4 |
| 1309 | 0x51d | Object_29 | 8 | 4 |
| 1310 | 0x51e | Object_30 | 8 | 4 |
| 1311 | 0x51f | Object_31 | 8 | 4 |
| 1312 | 0x520 | Object_32 | 8 | 4 |
| 1313 | 0x521 | Object_33 | 8 | 4 |
| 1314 | 0x522 | Object_34 | 8 | 4 |
| 1315 | 0x523 | Object_35 | 8 | 4 |
| 1316 | 0x524 | Object_36 | 8 | 4 |
| 1317 | 0x525 | Object_37 | 8 | 4 |
| 1318 | 0x526 | Object_38 | 8 | 4 |
| 1319 | 0x527 | Object_39 | 8 | 4 |
| 1320 | 0x528 | Object_40 | 8 | 4 |
| 1321 | 0x529 | Object_41 | 8 | 4 |
| 1322 | 0x52a | Object_42 | 8 | 4 |
| 1323 | 0x52b | Object_43 | 8 | 4 |
| 1324 | 0x52c | Object_44 | 8 | 4 |
| 1325 | 0x52d | Object_45 | 8 | 4 |
| 1326 | 0x52e | Object_46 | 8 | 4 |
| 1327 | 0x52f | Object_47 | 8 | 4 |
| 1328 | 0x530 | Object_48 | 8 | 4 |
| 1329 | 0x531 | Object_49 | 8 | 4 |
| 1330 | 0x532 | Object_50 | 8 | 4 |
| 1331 | 0x533 | Object_51 | 8 | 4 |
| 1332 | 0x534 | Object_52 | 8 | 4 |
| 1333 | 0x535 | Object_53 | 8 | 4 |
| 1334 | 0x536 | Object_54 | 8 | 4 |
| 1335 | 0x537 | Object_55 | 8 | 4 |
| 1336 | 0x538 | Object_56 | 8 | 4 |
| 1337 | 0x539 | Object_57 | 8 | 4 |
| 1338 | 0x53a | Object_58 | 8 | 4 |
| 1339 | 0x53b | Object_59 | 8 | 4 |
| 1340 | 0x53c | Object_60 | 8 | 4 |
| 1341 | 0x53d | Object_61 | 8 | 4 |
| 1342 | 0x53e | Object_62 | 8 | 4 |
| 1343 | 0x53f | Object_63 | 8 | 4 |

## ford_fusion_2018_pt — Ford Fusion 2018 [B]

- Make: ford; Powertrain bus
- Messages: 14; signals: 67
- Evidence: opendbc/opendbc/dbc/ford_fusion_2018_pt.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 130 | 0x82 | EPAS_INFO | 8 | 10 |
| 118 | 0x76 | Steering_Wheel_Data_CG1 | 8 | 5 |
| 131 | 0x83 | Steering_Buttons | 8 | 8 |
| 145 | 0x91 | Yaw_Data | 8 | 3 |
| 146 | 0x92 | Accel_Data | 8 | 6 |
| 357 | 0x165 | Cruise_Status | 8 | 3 |
| 516 | 0x204 | EngineData_14 | 8 | 1 |
| 535 | 0x217 | WheelSpeed_CG1 | 8 | 4 |
| 534 | 0x216 | WheelData | 8 | 9 |
| 947 | 0x3b3 | Doors | 8 | 4 |
| 963 | 0x3c3 | BCM_to_HS_Body | 8 | 1 |
| 970 | 0x3ca | Lane_Keep_Assist_Control | 8 | 4 |
| 972 | 0x3cc | Lane_Keep_Assist_Status | 8 | 3 |
| 984 | 0x3d8 | Lane_Keep_Assist_Ui | 8 | 6 |

## ford_lincoln_base_pt — Ford/Lincoln [B]

- Make: ford; Base powertrain DBC
- Messages: 331; signals: 2150
- Evidence: opendbc/opendbc/dbc/ford_lincoln_base_pt.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 823 | 0x337 | DTE_HPCMtoECG | 8 | 7 |
| 824 | 0x338 | DTE_ECGtoHPCM | 8 | 14 |
| 949 | 0x3b5 | Tire_Pressure_Data_FD1 | 8 | 4 |
| 1825 | 0x721 | TesterPhysicalReqVDM_FD1 | 64 | 1 |
| 524 | 0x20c | AWD_Torque_Data | 8 | 3 |
| 740 | 0x2e4 | PHEV_Battery_Data1_FD1 | 8 | 1 |
| 1160 | 0x488 | ECG_Data2_FD1 | 8 | 3 |
| 776 | 0x308 | SmartChargingData_ECG_3 | 8 | 10 |
| 775 | 0x307 | SmartChargingData_ECG_2 | 8 | 7 |
| 774 | 0x306 | SmartChargingData_ECG_1 | 8 | 8 |
| 811 | 0x32b | APIM_Data_FD1 | 8 | 10 |
| 850 | 0x352 | HEV_ChargeStat_FD1 | 8 | 5 |
| 563 | 0x233 | MasterReset_HS3_ECGDat_FD1 | 8 | 5 |
| 1833 | 0x729 | TesterPhysicalResVDM | 64 | 1 |
| 570 | 0x23a | Suspension_Data | 8 | 7 |
| 837 | 0x345 | VeyDynamics_Data | 8 | 5 |
| 885 | 0x375 | ECG_Data3_FD1 | 8 | 9 |
| 1150 | 0x47e | LocationServices_Data1_FD1 | 8 | 1 |
| 542 | 0x21e | LocationServices_3_FD1 | 8 | 1 |
| 2612224016 | 0x9bb36010 | PARSEDPushPCMtoGWM_ECG | 8 | 1 |
| 810 | 0x32a | ECG_Data_FD1 | 8 | 12 |
| 550 | 0x226 | ECG_Data4_FD1 | 8 | 1 |
| 639 | 0x27f | OffBrdChrg_Signals2 | 8 | 11 |
| 530 | 0x212 | OffBrdChrg_Signals | 8 | 8 |
| 1142 | 0x476 | ConsTip_Data_FD1 | 8 | 1 |
| 817 | 0x331 | Locking_Systems_2_FD1 | 8 | 20 |
| 879 | 0x36f | BCMC_Data_FD1 | 8 | 2 |
| 878 | 0x36e | DCACA_Data4 | 8 | 13 |
| 395 | 0x18b | HeadUpDisplayReq_FD1 | 8 | 1 |
| 2611055832 | 0x9ba18cd8 | PARSEDPhysGWM_ECGtoSODR | 8 | 1 |
| 2611054808 | 0x9ba188d8 | PARSEDPhysGWM_ECGtoSODL | 8 | 1 |
| 2611026136 | 0x9ba118d8 | PARSEDPhysGWM_ECGtoSODCMD | 8 | 1 |
| 2611025112 | 0x9ba114d8 | PARSEDPhysGWM_ECGtoSODCMC | 8 | 1 |
| 2610975960 | 0x9ba054d8 | PARSEDPhysGWM_ECGtoCCM | 8 | 1 |
| 2610007256 | 0x9b918cd8 | OTAPhysGWM_ECGtoSODR | 8 | 1 |
| 2610006232 | 0x9b9188d8 | OTAPhysGWM_ECGtoSODL | 8 | 1 |
| 2609977560 | 0x9b9118d8 | OTAPhysGWM_ECGtoSODCMD | 8 | 1 |
| 2609976536 | 0x9b9114d8 | OTAPhysGWM_ECGtoSODCMC | 8 | 1 |
| 2609927384 | 0x9b9054d8 | OTAPhysGWM_ECGtoCCM | 8 | 1 |
| 2611175523 | 0x9ba36063 | PARSEDPhysSODRtoGWM_ECG | 8 | 1 |
| 2612224099 | 0x9bb36063 | PARSEDPushSODRtoGWM_ECG | 8 | 1 |
| 2611175522 | 0x9ba36062 | PARSEDPhysSODLtoGWM_ECG | 8 | 1 |
| 2612224098 | 0x9bb36062 | PARSEDPushSODLtoGWM_ECG | 8 | 1 |
| 2611175494 | 0x9ba36046 | PARSEDPhysSODCMDtoGWM_ECG | 8 | 1 |
| 2612224070 | 0x9bb36046 | PARSEDPushSODCMDtoGWM | 8 | 1 |
| 2611175493 | 0x9ba36045 | PARSEDPhysSODCMCtoGWM_ECG | 8 | 1 |
| 2612224069 | 0x9bb36045 | PARSEDPushSODCMCtoGWM | 8 | 1 |
| 2611175445 | 0x9ba36015 | PARSEDPhysCCMtoGWM_ECG | 8 | 1 |
| 2612224021 | 0x9bb36015 | PARSEDPushCCMtoGWM_ECG | 8 | 1 |
| 2610126947 | 0x9b936063 | OTAPhysSODRtoGWM_ECG | 8 | 1 |
| 2610126946 | 0x9b936062 | OTAPhysSODLtoGWM_ECG | 8 | 1 |
| 2610126918 | 0x9b936046 | OTAPhysSODCMDtoGWM_ECG | 8 | 1 |
| 2610126917 | 0x9b936045 | OTAPhysSODCMCtoGWM_ECG | 8 | 1 |
| 2610126869 | 0x9b936015 | OTAPhysCCMtoGWM_ECG | 8 | 1 |
| 984 | 0x3d8 | IPMA_Data | 8 | 15 |
| 985 | 0x3d9 | IPMA_Data2 | 8 | 15 |
| 992 | 0x3e0 | Personality_Data_FD1 | 8 | 4 |
| 2612019416 | 0x9bb040d8 | PARSEDPushFcGWM_ECGtoPCM | 8 | 1 |
| 943 | 0x3af | IPMA_Data4 | 8 | 4 |
| 515 | 0x203 | PowertrainData_12 | 8 | 3 |
| 1111 | 0x457 | TrailerAid_Stat2_FD1 | 8 | 5 |
| 1106 | 0x452 | TrailerAid_Stat1_FD1 | 8 | 1 |
| 1985 | 0x7c1 | TesterPhysicalReqCMR_DSMC | 64 | 1 |
| 1993 | 0x7c9 | TesterPhysicalResCMR_DSMC | 64 | 1 |
| 1104 | 0x450 | DrvStatMonData | 8 | 11 |
| 1503 | 0x5df | CMR_DSMC_AutoSar_NetwrkMgt | 8 | 8 |
| 2610995416 | 0x9ba0a0d8 | PARSEDPhysGWM_ECGtoABS | 8 | 1 |
| 2612043992 | 0x9bb0a0d8 | PARSEDPushFcGWM_ECGtoABS | 8 | 1 |
| 2609946840 | 0x9b90a0d8 | OTAPhysGWM_ECGtoABS | 8 | 1 |
| 2611175464 | 0x9ba36028 | PARSEDPhysABStoGWM_ECG | 8 | 1 |
| 2612224040 | 0x9bb36028 | PARSEDPushABStoGWM_ECG | 8 | 1 |
| 2610126888 | 0x9b936028 | OTAPhysABStoGWM_ECG | 8 | 1 |
| 2610988248 | 0x9ba084d8 | PARSEDPhysGWM_ECGtoIPMA | 8 | 1 |
| 2609939672 | 0x9b9084d8 | OTAPhysGWM_ECGtoIPMA | 8 | 1 |
| 1114 | 0x45a | TrailerAid_Data_FD1 | 8 | 2 |
| 1116 | 0x45c | TrailerAid_Data3_FD1 | 8 | 12 |
| 2611175457 | 0x9ba36021 | PARSEDPhysIPMAtoGWM_ECG | 8 | 1 |
| 2612224033 | 0x9bb36021 | PARSEDPushIPMAtoGWM_ECG | 8 | 1 |
| 2610126881 | 0x9b936021 | OTAPhysIPMAtoGWM_ECG | 8 | 1 |
| 1085 | 0x43d | Low_Voltage_Power_Data_FD1 | 8 | 8 |
| 791 | 0x317 | Cluster_HEV_Data8_FD1 | 8 | 5 |
| 2610970840 | 0x9ba040d8 | PARSEDPhysGWM_ECGtoPCM | 8 | 1 |
| 2609922264 | 0x9b9040d8 | OTAPhysGWM_ECGtoPCM | 8 | 1 |
| 868 | 0x364 | BattRgenLo_4_FD1 | 8 | 10 |
| 867 | 0x363 | BattRgenLo_3_FD1 | 8 | 6 |
| 866 | 0x362 | BattRgenLo_2_FD1 | 8 | 5 |
| 865 | 0x361 | BattRgenLo_1_FD1 | 8 | 2 |
| 2611175440 | 0x9ba36010 | PARSEDPhysPCMtoGWM_ECG | 8 | 1 |
| 2610126864 | 0x9b936010 | OTAPhysPCMtoGWM_ECG | 8 | 1 |
| 2611175441 | 0x9ba36011 | PARSEDHPCMtoGWM_ECG_FD1 | 8 | 1 |
| 2612224017 | 0x9bb36011 | PARSEDPushSOBDMCtoGWM_FD1 | 8 | 1 |
| 2610126865 | 0x9b936011 | OTAPhysSOBDMCtoGWM_FD1 | 8 | 1 |
| 1679 | 0x68f | SOBDMC_RapidData_Resp4_FD1 | 8 | 1 |
| 1678 | 0x68e | SOBDMC_RapidData_Resp3_FD1 | 8 | 1 |
| 1677 | 0x68d | SOBDMC_RapidData_Resp2_FD1 | 8 | 1 |
| 1676 | 0x68c | SOBDMC_RapidData_Resp1_FD1 | 8 | 1 |
| 1445 | 0x5a5 | SOBDMC_AutoSar_NetMgmt_FD1 | 8 | 8 |
| 1144 | 0x478 | MHT_EV_Wakeup_FD1 | 8 | 17 |
| 1141 | 0x475 | Cluster_HEV_Data9_FD1 | 8 | 4 |
| 1140 | 0x474 | Cluster_HEV_Data7_FD1 | 8 | 3 |
| 1139 | 0x473 | GWM_HPCM_i_FrP11_FD1 | 8 | 7 |
| 1138 | 0x472 | GWM_HPCM_i_FrP10_FD1 | 8 | 7 |
| 1089 | 0x441 | MtrTracData_1_FD1 | 8 | 9 |
| 1088 | 0x440 | PreCond_Hev_Data1_FD1 | 8 | 8 |
| 1040 | 0x410 | AC_Compressor_Req_FD1 | 8 | 2 |
| 1016 | 0x3f8 | GoTimeSettings_FD1 | 8 | 12 |
| 1013 | 0x3f5 | ChargeSettings_FD1 | 8 | 8 |
| 1012 | 0x3f4 | Saved_Charge_Location_FD1 | 8 | 9 |
| 1011 | 0x3f3 | Unsaved_Charge_LocationFD1 | 8 | 7 |
| 871 | 0x367 | Cluster_HEV_Data4_FD1 | 8 | 4 |
| 786 | 0x312 | Cluster_HEV_Data1_FD1 | 8 | 3 |
| 72 | 0x48 | Global_PATS_Target2_FD1 | 8 | 3 |
| 912 | 0x390 | PowerDist_Data1_FD1 | 8 | 3 |
| 874 | 0x36a | PowerDistData_2_FD1 | 8 | 14 |
| 651 | 0x28b | TCU_Send_Signals_FD1 | 8 | 3 |
| 529 | 0x211 | APIM_Request_Signals_5_FD1 | 8 | 9 |
| 66 | 0x42 | Global_PATS_Ctrl_Info2_FD1 | 8 | 2 |
| 2610971864 | 0x9ba044d8 | PARSEDPhysGWMtoSOBDMC_FD1 | 8 | 1 |
| 2612002008 | 0x9baffcd8 | PARSEDFuncGWM_ECG_FD1 | 8 | 1 |
| 2609923288 | 0x9b9044d8 | OTAPhysGWM_ECGtoSOBDMC_FD1 | 8 | 1 |
| 2610953432 | 0x9b9ffcd8 | OTAFuncGWM_ECG_FD1 | 8 | 1 |
| 2022 | 0x7e6 | TesterPhysicalReqSOBDMC_FD | 64 | 1 |
| 1124 | 0x464 | APIMGPS_Data_Nav_3_FD1 | 8 | 7 |
| 1119 | 0x45f | Voltage_Power_Data2_FD1 | 8 | 2 |
| 132 | 0x84 | GlobalClock_Data_FD1 | 8 | 5 |
| 1990 | 0x7c6 | TesterPhysicalReqSODR | 64 | 1 |
| 1892 | 0x764 | TesterPhysicalReqCCM | 64 | 1 |
| 1798 | 0x706 | TesterPhysicalReqIPMA | 64 | 1 |
| 1123 | 0x463 | APIMGPS_Data_Nav_2_FD1 | 8 | 10 |
| 1122 | 0x462 | APIMGPS_Data_Nav_1_FD1 | 8 | 8 |
| 1003 | 0x3eb | Personality_BCM2_Data_FD1 | 8 | 16 |
| 994 | 0x3e2 | Personality_APIM_Data_FD1 | 8 | 9 |
| 778 | 0x30a | ParkAid_Aud_Warn_CmdM_FD1 | 8 | 7 |
| 549 | 0x225 | IPC_Infotainment_FD1 | 8 | 8 |
| 551 | 0x227 | APIM_Request_Signals_1_FD1 | 8 | 14 |
| 1010 | 0x3f2 | IPMA_Data3 | 8 | 8 |
| 1070 | 0x42e | Battery_Mgmt_24V_FD1 | 8 | 7 |
| 1186 | 0x4a2 | Driveline_Data_2 | 8 | 6 |
| 611 | 0x263 | Driveline_Data_1 | 8 | 13 |
| 1461 | 0x5b5 | PSCM_AutoSar_NetwrkMgmt | 8 | 8 |
| 1047 | 0x417 | TrailerAid_Data2 | 8 | 11 |
| 972 | 0x3cc | Lane_Assist_Data3_FD1 | 8 | 12 |
| 130 | 0x82 | EPAS_INFO | 8 | 16 |
| 126 | 0x7e | SteeringPinion_Data | 8 | 6 |
| 133 | 0x85 | SteeringPinion_Data_Alt | 8 | 6 |
| 1430 | 0x596 | ABS_AutoSar_NetworkMgt | 8 | 8 |
| 1200 | 0x4b0 | ABS_BrkBst_Data | 8 | 8 |
| 1102 | 0x44e | SelectDriveModeData2 | 8 | 12 |
| 1056 | 0x420 | SelectDriveModeData | 8 | 21 |
| 1054 | 0x41e | BrakeSysFeatures_3 | 8 | 15 |
| 1046 | 0x416 | BrakeSysFeatures_2 | 8 | 21 |
| 1045 | 0x415 | BrakeSysFeatures | 8 | 9 |
| 1044 | 0x414 | BrakeSnData_6 | 8 | 4 |
| 1042 | 0x412 | TrailerBrakeData | 8 | 3 |
| 535 | 0x217 | WheelSpeed | 8 | 4 |
| 534 | 0x216 | WheelData | 8 | 10 |
| 532 | 0x214 | DesiredTorqBrk_2 | 8 | 5 |
| 531 | 0x213 | DesiredTorqBrk | 8 | 31 |
| 136 | 0x88 | ActiveFronSteering_Req | 8 | 3 |
| 125 | 0x7d | BrakeSnData_4 | 8 | 7 |
| 119 | 0x77 | BrakeSnData_3 | 8 | 5 |
| 118 | 0x76 | BrakeSnData_5 | 8 | 7 |
| 73 | 0x49 | Global_PATS_SubTarget | 8 | 2 |
| 1034 | 0x40a | GGCC_Config_Mgmt_ID_1_FD1 | 8 | 1 |
| 1440 | 0x5a0 | TCM_AutoSar_NetworkMgt | 8 | 8 |
| 561 | 0x231 | TransGearData_2 | 8 | 2 |
| 330 | 0x14a | TransData_3 | 8 | 1 |
| 1090 | 0x442 | MtrTrac_Data2_FD1 | 8 | 5 |
| 870 | 0x366 | Cluster_HEV_Data3_FD1 | 8 | 3 |
| 869 | 0x365 | Cluster_HEV_Data2 | 8 | 9 |
| 606 | 0x25e | HEV_Powertrain_Data8_FD1 | 8 | 2 |
| 374 | 0x176 | PowertrainData_10 | 8 | 9 |
| 603 | 0x25b | HEV_Powertrain_Data2 | 8 | 3 |
| 602 | 0x25a | HEV_Powertrain_Data | 8 | 3 |
| 1152 | 0x480 | HEV_Powertrain_Data6 | 8 | 5 |
| 872 | 0x368 | Cluster_HEV_Data5 | 8 | 2 |
| 560 | 0x230 | TransGearData | 8 | 5 |
| 369 | 0x171 | EngineData_1 | 8 | 7 |
| 92 | 0x5c | Gear_Shift_by_Wire_3 | 8 | 15 |
| 2030 | 0x7ee | TesterPhysicalResSOBDMCFD1 | 64 | 1 |
| 1087 | 0x43f | Powertrain_Data_5 | 8 | 11 |
| 332 | 0x14c | CGEA_Urea_Strategy | 8 | 10 |
| 1896 | 0x768 | TesterPhysicalResABS | 64 | 1 |
| 1889 | 0x761 | TesterPhysicalReqTCCM | 64 | 1 |
| 1888 | 0x760 | TesterPhysicalReqABS | 64 | 1 |
| 1848 | 0x738 | TesterPhysicalResPSCM | 64 | 1 |
| 1840 | 0x730 | TesterPhysicalReqPSCM | 64 | 1 |
| 1713 | 0x6b1 | ABS_Rapid_Data_Response_2 | 8 | 1 |
| 1712 | 0x6b0 | ABS_Rapid_Data_Response_1 | 8 | 1 |
| 2025 | 0x7e9 | TesterPhysicalResTCM | 64 | 1 |
| 2024 | 0x7e8 | TesterPhysicalResPCM | 64 | 1 |
| 2017 | 0x7e1 | TesterPhysicalReqTCM | 64 | 1 |
| 2016 | 0x7e0 | TesterPhysicalReqPCM | 64 | 1 |
| 2015 | 0x7df | TesterFunctionalReq_FD1 | 64 | 1 |
| 1897 | 0x769 | TesterPhysicalResTCCM | 64 | 1 |
| 1814 | 0x716 | TesterPhysicalReqGWM_FD1 | 64 | 1 |
| 1701 | 0x6a5 | TCM_Rapid_Data_Response_2 | 8 | 1 |
| 1700 | 0x6a4 | TCM_Rapid_Data_Response_1 | 8 | 1 |
| 1697 | 0x6a1 | PCM_Rapid_Data_Response_2 | 8 | 1 |
| 1696 | 0x6a0 | PCM_Rapid_Data_Response_1 | 8 | 1 |
| 1429 | 0x595 | PCM_AutoSar_NetworkMgmt | 8 | 8 |
| 1100 | 0x44c | PowertrainData_9 | 8 | 9 |
| 1098 | 0x44a | EffDrvModeData | 8 | 8 |
| 1086 | 0x43e | PowertrainData_3 | 8 | 4 |
| 1071 | 0x42f | Engine_Clutch_Data | 8 | 5 |
| 1069 | 0x42d | PowertrainData_2 | 8 | 11 |
| 1060 | 0x424 | Powertrain_Data_4 | 8 | 7 |
| 1057 | 0x421 | PowertrainData_1 | 8 | 12 |
| 1055 | 0x41f | PowertrainData_7 | 8 | 7 |
| 562 | 0x232 | PowertrainData_11 | 8 | 3 |
| 523 | 0x20b | Engine_Data_18 | 8 | 5 |
| 517 | 0x205 | PowertrainData_6 | 8 | 3 |
| 516 | 0x204 | EngVehicleSpThrottle | 8 | 8 |
| 514 | 0x202 | EngVehicleSpThrottle2 | 8 | 10 |
| 512 | 0x200 | TorqueDataEngFlags | 8 | 5 |
| 381 | 0x17d | EngineData_17 | 8 | 6 |
| 380 | 0x17c | EngineData_16 | 8 | 5 |
| 377 | 0x179 | EngineData_7 | 8 | 9 |
| 376 | 0x178 | EngineClimateData | 8 | 11 |
| 373 | 0x175 | EngineData_11 | 8 | 4 |
| 359 | 0x167 | VehicleOperatingModes | 8 | 9 |
| 358 | 0x166 | Stop_Start | 8 | 7 |
| 357 | 0x165 | EngBrakeData | 8 | 12 |
| 355 | 0x163 | EngineData_10 | 8 | 6 |
| 342 | 0x156 | EngineData_6 | 8 | 5 |
| 71 | 0x47 | Global_PATS_TargetInfo | 8 | 3 |
| 1822 | 0x71e | TesterPhysicalResGWM_FD1 | 64 | 1 |
| 1438 | 0x59e | GWM_AutoSar_NetMgmt_FD1 | 8 | 8 |
| 954 | 0x3ba | Body_Info_10_FD1 | 8 | 3 |
| 1006 | 0x3ee | Personality_IPMB_Data | 8 | 3 |
| 820 | 0x334 | Adaptive_Headlamp_Stat | 8 | 4 |
| 137 | 0x89 | ActiveFrontStrg_Stat_FD1 | 8 | 5 |
| 129 | 0x81 | Steering_Wheel_Data2_FD1 | 8 | 21 |
| 935 | 0x3a7 | Side_Detect_R_Stat | 8 | 15 |
| 1108 | 0x454 | RCMSerialNumber_FD1 | 8 | 8 |
| 261 | 0x105 | APIM_Request_Signals_FD1 | 8 | 11 |
| 1146 | 0x47a | TrailerInfo_2_FD1 | 8 | 2 |
| 533 | 0x215 | APIM_Send_Signals_2_FD1 | 8 | 25 |
| 1041 | 0x411 | AC_Compressor_Data_FD1 | 8 | 14 |
| 1067 | 0x42b | Battery_Mgmt_4_FD1 | 8 | 9 |
| 1112 | 0x458 | Battery_Traction_6_FD1 | 8 | 7 |
| 139 | 0x8b | CruiseCtrl_Strg_Data_FD1 | 8 | 28 |
| 1121 | 0x461 | AllTerrainControlData_FD1 | 8 | 3 |
| 1120 | 0x460 | FourByFourSwitchData_FD1 | 8 | 6 |
| 1050 | 0x41a | Climate_Control_Data_FD1 | 8 | 10 |
| 1137 | 0x471 | Cluster_HEV_Data10_FD1 | 8 | 1 |
| 1255 | 0x4e7 | BoundaryAlert_Right_4 | 8 | 11 |
| 1254 | 0x4e6 | BoundaryAlert_Right_3 | 8 | 11 |
| 1253 | 0x4e5 | BoundaryAlert_Right_2 | 8 | 11 |
| 1252 | 0x4e4 | BoundaryAlert_Right_1 | 8 | 11 |
| 1251 | 0x4e3 | BoundaryAlert_Left_4 | 8 | 11 |
| 1250 | 0x4e2 | BoundaryAlert_Left_3 | 8 | 11 |
| 1249 | 0x4e1 | BoundaryAlert_Left_2 | 8 | 11 |
| 1248 | 0x4e0 | BoundaryAlert_Left_1 | 8 | 11 |
| 1113 | 0x459 | TrailerAid_Stat3 | 8 | 11 |
| 1105 | 0x451 | Image_Processing_Data | 8 | 15 |
| 938 | 0x3aa | ParkAid_Aud_Warn_Stat | 8 | 17 |
| 939 | 0x3ab | ParkAid_Aud_Warn_Stat2 | 8 | 16 |
| 937 | 0x3a9 | ParkAid_Data_2 | 8 | 5 |
| 936 | 0x3a8 | ParkAid_Data | 8 | 18 |
| 877 | 0x36d | HEV_Powertrain_Data7_FD1 | 8 | 8 |
| 589 | 0x24d | Battery_Traction_5_FD1 | 8 | 4 |
| 588 | 0x24c | Battery_Traction_4_FD1 | 8 | 3 |
| 587 | 0x24b | Battery_Traction_3_FD1 | 8 | 7 |
| 389 | 0x185 | PreCond_Hev_Data2_FD1 | 8 | 10 |
| 1009 | 0x3f1 | APIM_Send_Signals1_FD1 | 8 | 9 |
| 360 | 0x168 | Gear_Shift_by_Wire_2_FD1 | 8 | 3 |
| 122 | 0x7a | Battery_Traction_1_FD1 | 8 | 8 |
| 90 | 0x5a | Gear_Shift_by_Wire_FD1 | 8 | 28 |
| 1091 | 0x443 | TrailerInfo_FD1 | 8 | 7 |
| 138 | 0x8a | ActiveFrontStrg_Stat2_FD1 | 8 | 2 |
| 131 | 0x83 | Steering_Data_FD1 | 8 | 34 |
| 787 | 0x313 | Power_Liftgate_Stat_FD1 | 8 | 5 |
| 953 | 0x3b9 | Body_Info_8_FD1 | 8 | 9 |
| 1093 | 0x445 | TrailerBrakeInfo_FD1 | 8 | 10 |
| 792 | 0x318 | IPC_Send_Signals_2_FD1 | 8 | 3 |
| 968 | 0x3c8 | Cluster_Lighting_Rq_FD1 | 8 | 2 |
| 819 | 0x333 | Pass_Dr_Stat_FD1 | 8 | 9 |
| 818 | 0x332 | Driver_Dr_Stat_FD1 | 8 | 10 |
| 806 | 0x326 | Compressor_Req_FD1 | 8 | 10 |
| 765 | 0x2fd | Mc_Send_Signals_2_FD1 | 8 | 17 |
| 559 | 0x22f | ElecHorizon_Data2_FD1 | 8 | 1 |
| 558 | 0x22e | ElecHorizon_Data1_FD1 | 8 | 1 |
| 934 | 0x3a6 | Side_Detect_L_Stat | 8 | 15 |
| 1072 | 0x430 | Cluster_Info1_FD1 | 8 | 22 |
| 909 | 0x38d | Body_Info_6_FD1 | 8 | 15 |
| 963 | 0x3c3 | BCM_Lamp_Stat_FD1 | 8 | 35 |
| 145 | 0x91 | Yaw_Data_FD1 | 8 | 6 |
| 76 | 0x4c | RCMStatusMessage2_FD1 | 8 | 11 |
| 65 | 0x41 | Global_PATS_Cntrl_Info_FD1 | 8 | 2 |
| 1076 | 0x434 | Cluster_Info_3_FD1 | 8 | 14 |
| 862 | 0x35e | Climate_Cntrl_Data_2_FD1 | 8 | 7 |
| 931 | 0x3a3 | Body_Info_9_FD1 | 8 | 11 |
| 578 | 0x242 | Body_Info_4_FD1 | 8 | 15 |
| 947 | 0x3b3 | BodyInfo_3_FD1 | 8 | 31 |
| 1084 | 0x43c | Battery_Mgmt_3_FD1 | 8 | 9 |
| 1068 | 0x42c | Battery_Mgmt_2_FD1 | 8 | 14 |
| 146 | 0x92 | Accel_Data_FD1 | 8 | 8 |
| 1900 | 0x76c | TesterPhysicalResCCM | 64 | 1 |
| 1806 | 0x70e | TesterPhysicalResIPMA | 64 | 1 |
| 997 | 0x3e5 | Personality_CCM_Data | 8 | 3 |
| 983 | 0x3d7 | Steer_Assist_Data | 8 | 8 |
| 982 | 0x3d6 | LateralMotionControl2 | 8 | 10 |
| 981 | 0x3d5 | GlareFreeBeam | 8 | 8 |
| 980 | 0x3d4 | AutoDriveBeam_Data1 | 8 | 10 |
| 979 | 0x3d3 | LateralMotionControl | 8 | 9 |
| 976 | 0x3d0 | SuspensionRoad_Data | 8 | 8 |
| 973 | 0x3cd | Traffic_RecognitnData | 8 | 18 |
| 970 | 0x3ca | Lane_Assist_Data1 | 8 | 7 |
| 962 | 0x3c2 | AutoDriveBeam_Data3 | 8 | 10 |
| 961 | 0x3c1 | AutoDriveBeam_Data2 | 8 | 10 |
| 394 | 0x18a | ACCDATA_3 | 8 | 26 |
| 391 | 0x187 | ACCDATA_2 | 8 | 11 |
| 390 | 0x186 | ACCDATA | 8 | 17 |
| 1441 | 0x5a1 | TCCM_AutoSar_NetwkMgmt | 8 | 8 |
| 1787 | 0x6fb | TesterPhysicalResSODCMD | 64 | 1 |
| 1779 | 0x6f3 | TesterPhysicalReqSODCMD | 64 | 1 |
| 1786 | 0x6fa | TesterPhysicalResSODCMC | 64 | 1 |
| 1778 | 0x6f2 | TesterPhysicalReqSODCMC | 64 | 1 |
| 1153 | 0x481 | All_Terrain_Data_FD1 | 8 | 1 |
| 942 | 0x3ae | ParkAid_Data2 | 8 | 5 |
| 930 | 0x3a2 | Bndry_Alert_R_Data | 8 | 14 |
| 929 | 0x3a1 | Bndry_Alert_L_Data | 8 | 14 |
| 402 | 0x192 | Dsp_Request_Signals11_FD1 | 8 | 9 |
| 924 | 0x39c | DCACA_Data3_FD1 | 8 | 4 |
| 923 | 0x39b | DCACA_Data2_FD1 | 8 | 4 |
| 1998 | 0x7ce | TesterPhysicalResSODR | 64 | 1 |
| 1996 | 0x7cc | TesterPhysicalResSODL | 64 | 1 |
| 1988 | 0x7c4 | TesterPhysicalReqSODL | 64 | 1 |
| 922 | 0x39a | DCACA_Data1_FD1 | 8 | 13 |
| 1082 | 0x43a | INSTRUMENT_PANEL | 8 | 1 |

## chrysler_cusw — Chrysler CUSW [B]

- Make: stellantis; Compact US Wide platform (Dart, Cherokee KL, 200)
- Messages: 26; signals: 97
- Evidence: opendbc/opendbc/dbc/chrysler_cusw.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 492 | 0x1ec | EPS_STATUS | 8 | 8 |
| 1250 | 0x4e2 | DOORS | 8 | 5 |
| 1262 | 0x4ee | GEAR | 8 | 1 |
| 875 | 0x36b | SEATBELT_STATUS | 8 | 1 |
| 1264 | 0x4f0 | STEERING_LEVERS | 7 | 2 |
| 480 | 0x1e0 | TRACTION_BUTTON | 8 | 1 |
| 740 | 0x2e4 | WHEEL_SPEEDS_REAR | 8 | 4 |
| 520 | 0x208 | EPS_STATUS_2 | 7 | 5 |
| 494 | 0x1ee | STEERING | 6 | 4 |
| 738 | 0x2e2 | BRAKE_2 | 8 | 5 |
| 742 | 0x2e6 | WHEEL_SPEEDS_FRONT | 8 | 4 |
| 502 | 0x1f6 | LKAS_COMMAND | 4 | 4 |
| 1498 | 0x5da | LKAS_1 | 2 | 0 |
| 1500 | 0x5dc | DAS_6 | 4 | 4 |
| 1508 | 0x5e4 | LKAS_HEARTBIT | 8 | 1 |
| 762 | 0x2fa | CRUISE_BUTTONS | 3 | 10 |
| 484 | 0x1e4 | BRAKE_1 | 8 | 4 |
| 488 | 0x1e8 | BRAKE_3 | 5 | 4 |
| 500 | 0x1f4 | GEARBOX_1 | 7 | 4 |
| 510 | 0x1fe | ACCEL_GAS | 5 | 5 |
| 490 | 0x1ea | DASHBOARD | 4 | 1 |
| 1006 | 0x3ee | ACC_HUD | 7 | 4 |
| 748 | 0x2ec | ACC_CONTROL | 8 | 10 |
| 496 | 0x1f0 | CLUSTER_1 | 8 | 4 |
| 103596083 | 0x62cc033 | BSM_LEFT | 8 | 1 |
| 103596084 | 0x62cc034 | BSM_RIGHT | 7 | 1 |

## chrysler_pacifica_2017_hybrid_private_fusion — Chrysler Pacifica 2017 Hybrid [B]

- Make: stellantis; Private fusion DBC
- Messages: 31; signals: 122
- Evidence: opendbc/opendbc/dbc/chrysler_pacifica_2017_hybrid_private_fusion.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 544 | 0x220 | a_1 | 8 | 9 |
| 576 | 0x240 | b_1 | 8 | 6 |
| 608 | 0x260 | a_2 | 8 | 9 |
| 640 | 0x280 | b_2 | 8 | 6 |
| 644 | 0x284 | a_3 | 8 | 9 |
| 648 | 0x288 | b_3 | 8 | 6 |
| 652 | 0x28c | a_4 | 8 | 9 |
| 656 | 0x290 | b_4 | 8 | 6 |
| 512 | 0x200 | unknown_200 | 8 | 7 |
| 514 | 0x202 | unknown_202 | 8 | 3 |
| 706 | 0x2c2 | c_1 | 8 | 4 |
| 708 | 0x2c4 | c_2 | 8 | 4 |
| 710 | 0x2c6 | c_3 | 8 | 4 |
| 712 | 0x2c8 | c_4 | 8 | 4 |
| 714 | 0x2ca | c_5 | 8 | 4 |
| 716 | 0x2cc | c_6 | 8 | 4 |
| 718 | 0x2ce | c_7 | 8 | 4 |
| 720 | 0x2d0 | c_8 | 8 | 4 |
| 722 | 0x2d2 | c_9 | 8 | 4 |
| 724 | 0x2d4 | c_10 | 8 | 4 |
| 674 | 0x2a2 | d_1 | 8 | 1 |
| 676 | 0x2a4 | d_2 | 8 | 1 |
| 678 | 0x2a6 | d_3 | 8 | 1 |
| 680 | 0x2a8 | d_4 | 8 | 1 |
| 682 | 0x2aa | d_5 | 8 | 1 |
| 684 | 0x2ac | d_6 | 8 | 1 |
| 686 | 0x2ae | d_7 | 8 | 1 |
| 688 | 0x2b0 | d_8 | 8 | 1 |
| 690 | 0x2b2 | d_9 | 8 | 1 |
| 692 | 0x2b4 | d_10 | 8 | 1 |
| 672 | 0x2a0 | NEW_MSG_5 | 8 | 2 |

## fca_giorgio — FCA Giorgio [B]

- Make: stellantis; Giorgio platform (Giulia, Stelvio)
- Messages: 37; signals: 154
- Evidence: opendbc/opendbc/dbc/fca_giorgio.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 171 | 0xab | NEW_MSG_AB | 8 | 6 |
| 222 | 0xde | EPS_1 | 6 | 6 |
| 228 | 0xe4 | NEW_MSG_E4 | 6 | 1 |
| 238 | 0xee | ABS_1 | 8 | 6 |
| 241 | 0xf1 | NEW_MSG_F1 | 8 | 3 |
| 249 | 0xf9 | NEW_MSG_F9 | 4 | 2 |
| 250 | 0xfa | ABS_3 | 8 | 5 |
| 252 | 0xfc | ENGINE_1 | 8 | 7 |
| 254 | 0xfe | ABS_2 | 8 | 6 |
| 257 | 0x101 | ABS_6 | 8 | 5 |
| 262 | 0x106 | EPS_2 | 7 | 9 |
| 263 | 0x107 | ABS_4 | 8 | 1 |
| 265 | 0x109 | NEW_MSG_109 | 8 | 2 |
| 270 | 0x10e | ABS_7 | 7 | 5 |
| 278 | 0x116 | ABS_5 | 8 | 14 |
| 280 | 0x118 | NEW_MSG_118 | 6 | 2 |
| 282 | 0x11a | NEW_MSG_11A | 8 | 3 |
| 284 | 0x11c | NEW_MSG_11C | 8 | 7 |
| 288 | 0x120 | NEW_MSG_120 | 6 | 2 |
| 290 | 0x122 | EPS_3 | 4 | 3 |
| 501 | 0x1f5 | NEW_MSG_1F5 | 5 | 3 |
| 502 | 0x1f6 | LKA_COMMAND | 8 | 7 |
| 508 | 0x1fc | NEW_MSG_1FC | 8 | 1 |
| 601 | 0x259 | NEW_MSG_259 | 8 | 1 |
| 762 | 0x2fa | NEW_MSG_2FA | 3 | 1 |
| 766 | 0x2fe | CAM_UNKNOWN_1 | 4 | 0 |
| 900 | 0x384 | NEW_MSG_384 | 8 | 1 |
| 1040 | 0x410 | NEW_MSG_410 | 8 | 5 |
| 1046 | 0x416 | NEW_MSG_416 | 8 | 21 |
| 1194 | 0x4aa | CAM_UNKNOWN_2 | 8 | 0 |
| 1198 | 0x4ae | LKA_HUD_1 | 8 | 7 |
| 1351 | 0x547 | LKA_HUD_2 | 8 | 2 |
| 1442 | 0x5a2 | ACC_1 | 8 | 6 |
| 1458 | 0x5b2 | CAM_UNKNOWN_5 | 4 | 1 |
| 1854 | 0x73e | BCM_1 | 4 | 2 |
| 1865 | 0x749 | NEW_MSG_749 | 8 | 1 |
| 506855454 | 0x1e36001e | CAM_UNKNOWN_6 | 1 | 0 |

## toyota_2017_ref_pt — Toyota 2017 ref [B]

- Make: toyota; Reference powertrain DBC
- Messages: 143; signals: 1315
- Evidence: opendbc/opendbc/dbc/toyota_2017_ref_pt.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 1196 | 0x4ac | ABG1D50 | 8 | 8 |
| 1212 | 0x4bc | ABG1D51 | 8 | 8 |
| 945 | 0x3b1 | ABG1S01 | 8 | 6 |
| 836 | 0x344 | ACC1F01 | 8 | 20 |
| 1227 | 0x4cb | ACC1N01 | 8 | 4 |
| 835 | 0x343 | ACC1S03 | 8 | 15 |
| 896 | 0x380 | ACN1S01 | 8 | 17 |
| 897 | 0x381 | ACN1S04 | 8 | 33 |
| 944 | 0x3b0 | ACN1S07 | 6 | 6 |
| 1250 | 0x4e2 | AFS1N01 | 8 | 4 |
| 913 | 0x391 | AFS1S01 | 8 | 8 |
| 845 | 0x34d | AFS1S02 | 5 | 3 |
| 1044 | 0x414 | AHB1S01 | 8 | 3 |
| 900 | 0x384 | AVN1S01 | 6 | 15 |
| 902 | 0x386 | AVN1S03 | 6 | 21 |
| 911 | 0x38f | AVN1S07 | 8 | 12 |
| 905 | 0x389 | AVN1S08 | 8 | 24 |
| 998 | 0x3e6 | AVN1S11 | 5 | 7 |
| 933 | 0x3a5 | AVN1S13 | 8 | 11 |
| 936 | 0x3a8 | AVN1S16 | 5 | 6 |
| 999 | 0x3e7 | AVN1S17 | 7 | 9 |
| 1000 | 0x3e8 | AVN1S18 | 8 | 8 |
| 1001 | 0x3e9 | AVN1S19 | 8 | 8 |
| 1076 | 0x434 | AVN1S20 | 8 | 10 |
| 1077 | 0x435 | AVN1S21 | 8 | 21 |
| 1043 | 0x413 | AVN1S31 | 8 | 9 |
| 1075054137 | 0x40140639 | BDB1F01_14 | 8 | 13 |
| 1075185211 | 0x4016063b | BDB1F03_16 | 8 | 4 |
| 1074791968 | 0x40100620 | BDB1S01_10 | 8 | 18 |
| 1074857505 | 0x40110621 | BDB1S02_11 | 8 | 4 |
| 1074923042 | 0x40120622 | BDB1S03_12 | 8 | 17 |
| 1075381795 | 0x40190623 | BDB1S04_19 | 8 | 15 |
| 1074988600 | 0x40130638 | BDB1S05_13 | 8 | 17 |
| 1075250736 | 0x40170630 | BDB1S06_17 | 8 | 5 |
| 1075316273 | 0x40180631 | BDB1S07_18 | 8 | 8 |
| 1075447332 | 0x401a0624 | BDB1S08_1A | 8 | 11 |
| 1075643943 | 0x401d0627 | BDB1S11_1D | 8 | 4 |
| 1083704892 | 0x4098063c | BDB1S17_98 | 8 | 9 |
| 1083770429 | 0x4099063d | BDB1S18_99 | 8 | 7 |
| 1020 | 0x3fc | BDB1S19 | 8 | 3 |
| 1083835966 | 0x409a063e | BDB1S20_9A | 8 | 4 |
| 1083901503 | 0x409b063f | BDB1S21_9B | 8 | 10 |
| 1005 | 0x3ed | BGM1S01 | 2 | 4 |
| 1237 | 0x4d5 | BSR1N01 | 8 | 4 |
| 1014 | 0x3f6 | BSR1S01 | 8 | 3 |
| 1114 | 0x45a | CGW1N02 | 8 | 1 |
| 1228 | 0x4cc | CSR1N01 | 8 | 4 |
| 918 | 0x396 | CSR1S01 | 7 | 21 |
| 1087768273 | 0x40d606d1 | DMS1S02_D6 | 8 | 1 |
| 869 | 0x365 | DS11D70 | 7 | 14 |
| 870 | 0x366 | DS11D71 | 7 | 13 |
| 871 | 0x367 | DS11D72 | 2 | 7 |
| 643 | 0x283 | DS11F01 | 7 | 15 |
| 1041 | 0x411 | DS12F02 | 8 | 21 |
| 1042 | 0x412 | DS12F03 | 8 | 18 |
| 1207 | 0x4b7 | ECO1D50 | 8 | 8 |
| 355 | 0x163 | ECO1S01 | 5 | 8 |
| 922 | 0x39a | ECO1S90 | 8 | 14 |
| 1182 | 0x49e | ECT1D50 | 8 | 8 |
| 1183 | 0x49f | ECT1D51 | 8 | 8 |
| 1200 | 0x4b0 | ECT1D52 | 8 | 8 |
| 1201 | 0x4b1 | ECT1D53 | 8 | 8 |
| 1202 | 0x4b2 | ECT1D54 | 8 | 8 |
| 1203 | 0x4b3 | ECT1D55 | 8 | 8 |
| 464 | 0x1d0 | ECT1F03 | 8 | 22 |
| 725 | 0x2d5 | ECT1S10 | 2 | 1 |
| 956 | 0x3bc | ECT1S92 | 8 | 20 |
| 1176 | 0x498 | ENG1D50 | 8 | 8 |
| 1177 | 0x499 | ENG1D51 | 8 | 8 |
| 1178 | 0x49a | ENG1D52 | 8 | 8 |
| 1179 | 0x49b | ENG1D53 | 8 | 8 |
| 1180 | 0x49c | ENG1D54 | 8 | 8 |
| 1181 | 0x49d | ENG1D55 | 8 | 8 |
| 1192 | 0x4a8 | ENG1D56 | 8 | 8 |
| 1191 | 0x4a7 | ENG1D57 | 8 | 8 |
| 1197 | 0x4ad | ENG1D58 | 8 | 8 |
| 1198 | 0x4ae | ENG1D59 | 8 | 8 |
| 1199 | 0x4af | ENG1D60 | 8 | 8 |
| 1017 | 0x3f9 | ENG1F03 | 8 | 12 |
| 452 | 0x1c4 | ENG1F07 | 8 | 16 |
| 114 | 0x72 | ENG1F43 | 5 | 3 |
| 705 | 0x2c1 | ENG1S01 | 8 | 13 |
| 961 | 0x3c1 | ENG1S23 | 3 | 2 |
| 979 | 0x3d3 | ENG1S28 | 2 | 1 |
| 1408 | 0x580 | ENG1S51 | 8 | 8 |
| 1409 | 0x581 | ENG1S52 | 8 | 8 |
| 1410 | 0x582 | ENG1S54 | 8 | 3 |
| 955 | 0x3bb | ENG1S92 | 8 | 17 |
| 921 | 0x399 | ENG1S95 | 8 | 16 |
| 238 | 0xee | ENG2F01 | 4 | 4 |
| 466 | 0x1d2 | ENG2F04 | 8 | 18 |
| 467 | 0x1d3 | ENG2F05 | 8 | 13 |
| 119 | 0x77 | ENG2F41 | 6 | 6 |
| 120 | 0x78 | ENG2F42 | 4 | 5 |
| 916 | 0x394 | EPS1S90 | 1 | 1 |
| 1235 | 0x4d3 | FCM1N01 | 8 | 4 |
| 1161 | 0x489 | FCM1S10 | 8 | 13 |
| 1162 | 0x48a | FCM1S11 | 8 | 14 |
| 1163 | 0x48b | FCM1S12 | 8 | 9 |
| 1279 | 0x4ff | FRD1N01 | 8 | 4 |
| 737 | 0x2e1 | FWM1S01 | 2 | 10 |
| 1082263092 | 0x40820634 | IDT1S03_82 | 8 | 6 |
| 1082328629 | 0x40830635 | IDT1S04_83 | 8 | 3 |
| 1257 | 0x4e9 | KSS1N01 | 8 | 4 |
| 927 | 0x39f | KSS1S90 | 1 | 1 |
| 1263 | 0x4ef | MAV1N01 | 8 | 3 |
| 1075840528 | 0x40200610 | MET1S01_20 | 8 | 11 |
| 1075906065 | 0x40210611 | MET1S02_21 | 8 | 7 |
| 1076037145 | 0x40230619 | MET1S04_23 | 8 | 6 |
| 1076102682 | 0x4024061a | MET1S05_24 | 8 | 6 |
| 1076299282 | 0x40270612 | MET1S08_27 | 8 | 4 |
| 1076364819 | 0x40280613 | MET1S09_28 | 8 | 20 |
| 1076430356 | 0x40290614 | MET1S10_29 | 8 | 6 |
| 1076495893 | 0x402a0615 | MET1S11_2A | 8 | 7 |
| 1076561430 | 0x402b0616 | MET1S12_2B | 8 | 11 |
| 992 | 0x3e0 | MET1S18 | 8 | 9 |
| 1075840755 | 0x402006f3 | MET1S22_20 | 8 | 17 |
| 1088685760 | 0x40e406c0 | PMN1F03_E4 | 8 | 8 |
| 1193 | 0x4a9 | SCS1D50 | 8 | 8 |
| 1226 | 0x4ca | SCS1N01 | 8 | 4 |
| 744 | 0x2e8 | SCS1S01 | 8 | 2 |
| 815 | 0x32f | SCS1S06 | 5 | 3 |
| 917 | 0x395 | SCS1S90 | 4 | 7 |
| 37 | 0x25 | STR1S01 | 8 | 12 |
| 1059 | 0x423 | STR1S02 | 1 | 2 |
| 170 | 0xaa | VSC1F01 | 8 | 8 |
| 426 | 0x1aa | VSC1F02 | 6 | 13 |
| 550 | 0x226 | VSC1F06 | 8 | 16 |
| 180 | 0xb4 | VSC1S03 | 8 | 4 |
| 800 | 0x320 | VSC1S07 | 8 | 23 |
| 1056 | 0x420 | VSC1S08 | 8 | 10 |
| 186 | 0xba | VSC1S12 | 4 | 3 |
| 562 | 0x232 | VSC1S14 | 6 | 10 |
| 552 | 0x228 | VSC1S29 | 4 | 3 |
| 1168 | 0x490 | VSC1S92 | 1 | 3 |
| 951 | 0x3b7 | VSC1S95 | 8 | 18 |
| 1063 | 0x427 | VSC1S96 | 8 | 6 |
| 545 | 0x221 | VSC2F05 | 5 | 8 |
| 544 | 0x220 | VSC2F07 | 4 | 10 |
| 36 | 0x24 | YGS1S03 | 8 | 17 |
| 1073743490 | 0x40000682 | YGW1S01_0 | 8 | 7 |
| 1073743491 | 0x40000683 | YGW1S02_0 | 8 | 4 |
| 1073743494 | 0x40000686 | YGW1S05_0 | 8 | 5 |

## toyota_adas — Toyota [B]

- Make: toyota; ADAS bus
- Messages: 33; signals: 179
- Evidence: opendbc/opendbc/dbc/toyota_adas.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 291 | 0x123 | STATUS_MSG | 7 | 3 |
| 528 | 0x210 | TRACK_A_0 | 8 | 7 |
| 529 | 0x211 | TRACK_A_1 | 8 | 7 |
| 530 | 0x212 | TRACK_A_2 | 8 | 7 |
| 531 | 0x213 | TRACK_A_3 | 8 | 7 |
| 532 | 0x214 | TRACK_A_4 | 8 | 7 |
| 533 | 0x215 | TRACK_A_5 | 8 | 7 |
| 534 | 0x216 | TRACK_A_6 | 8 | 7 |
| 535 | 0x217 | TRACK_A_7 | 8 | 7 |
| 536 | 0x218 | TRACK_A_8 | 8 | 7 |
| 537 | 0x219 | TRACK_A_9 | 8 | 7 |
| 538 | 0x21a | TRACK_A_10 | 8 | 7 |
| 539 | 0x21b | TRACK_A_11 | 8 | 7 |
| 540 | 0x21c | TRACK_A_12 | 8 | 7 |
| 541 | 0x21d | TRACK_A_13 | 8 | 7 |
| 542 | 0x21e | TRACK_A_14 | 8 | 7 |
| 543 | 0x21f | TRACK_A_15 | 8 | 7 |
| 544 | 0x220 | TRACK_B_0 | 8 | 4 |
| 545 | 0x221 | TRACK_B_1 | 8 | 4 |
| 546 | 0x222 | TRACK_B_2 | 8 | 4 |
| 547 | 0x223 | TRACK_B_3 | 8 | 4 |
| 548 | 0x224 | TRACK_B_4 | 8 | 4 |
| 549 | 0x225 | TRACK_B_5 | 8 | 4 |
| 550 | 0x226 | TRACK_B_6 | 8 | 4 |
| 551 | 0x227 | TRACK_B_7 | 8 | 4 |
| 552 | 0x228 | TRACK_B_8 | 6 | 4 |
| 553 | 0x229 | TRACK_B_9 | 6 | 4 |
| 554 | 0x22a | TRACK_B_10 | 6 | 4 |
| 555 | 0x22b | TRACK_B_11 | 6 | 4 |
| 556 | 0x22c | TRACK_B_12 | 6 | 4 |
| 557 | 0x22d | TRACK_B_13 | 6 | 4 |
| 558 | 0x22e | TRACK_B_14 | 6 | 4 |
| 559 | 0x22f | TRACK_B_15 | 6 | 4 |

## toyota_iQ_2009_can — Toyota iQ 2009 [B]

- Make: toyota; Full-vehicle CAN
- Messages: 26; signals: 72
- Evidence: opendbc/opendbc/dbc/toyota_iQ_2009_can.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 1552 | 0x610 | CONTAINS_LRES_SPEED | 8 | 2 |
| 452 | 0x1c4 | ENGINE | 8 | 4 |
| 37 | 0x25 | STEERING | 8 | 6 |
| 36 | 0x24 | ACCELERATIONS | 8 | 4 |
| 947 | 0x3b3 | LOW_RES_INDICATORS | 8 | 2 |
| 955 | 0x3bb | BRAKING_PLUS_OTHER | 8 | 3 |
| 1595 | 0x63b | CONTAINS_TIME | 8 | 2 |
| 170 | 0xaa | WHEELS_SPEEDS | 8 | 4 |
| 180 | 0xb4 | VEHICLE_DYNAMICS | 8 | 4 |
| 186 | 0xba | NEW_MSG_9 | 8 | 1 |
| 426 | 0x1aa | NEW_MSG_5 | 8 | 1 |
| 906 | 0x38a | BOOLS | 8 | 5 |
| 979 | 0x3d3 | LOW_RES_ACCELERATOR | 8 | 1 |
| 1600 | 0x640 | SLOW_VARIABLE_INFOS | 8 | 2 |
| 1568 | 0x620 | DOORS | 8 | 11 |
| 705 | 0x2c1 | COMMAND | 8 | 5 |
| 928 | 0x3a0 | STEER2_MAYBE | 8 | 4 |
| 896 | 0x380 | LONG_TERM_2 | 8 | 1 |
| 944 | 0x3b0 | LONG_TERM_MSG | 8 | 1 |
| 1553 | 0x611 | TOTAL_DIST | 8 | 1 |
| 1572 | 0x624 | WHY_THESE_VALUES | 8 | 0 |
| 1555 | 0x613 | BETWEEN_RIDES_CHANGE_1 | 8 | 1 |
| 1090 | 0x442 | ASYNC_MSG_ACK | 8 | 2 |
| 1592 | 0x638 | NEW_MSG_14 | 8 | 2 |
| 608 | 0x260 | NEW_MSG_6 | 8 | 2 |
| 945 | 0x3b1 | BETWEEN_RIDES_CHANGES_2 | 8 | 1 |

## toyota_prius_2010_pt — Toyota Prius 2010 [B]

- Make: toyota; Powertrain bus
- Messages: 26; signals: 78
- Evidence: opendbc/opendbc/dbc/toyota_prius_2010_pt.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 36 | 0x24 | KINEMATICS | 8 | 3 |
| 166 | 0xa6 | BRAKE | 8 | 2 |
| 170 | 0xaa | WHEEL_SPEEDS | 8 | 4 |
| 180 | 0xb4 | SPEED | 8 | 3 |
| 295 | 0x127 | GEAR_PACKET | 8 | 4 |
| 466 | 0x1d2 | PCM_CRUISE | 8 | 4 |
| 550 | 0x226 | BRAKE_MODULE | 8 | 3 |
| 552 | 0x228 | ACCELEROMETER | 8 | 2 |
| 560 | 0x230 | BRAKE_MODULE2 | 8 | 1 |
| 581 | 0x245 | GAS_PEDAL | 8 | 1 |
| 608 | 0x260 | STEER_TORQUE_SENSOR | 8 | 4 |
| 610 | 0x262 | EPS_STATUS | 5 | 3 |
| 614 | 0x266 | STEERING_IPAS | 8 | 6 |
| 643 | 0x283 | PRE_COLLISION | 8 | 0 |
| 740 | 0x2e4 | STEERING_LKA | 8 | 6 |
| 742 | 0x2e6 | LEAD_INFO | 8 | 3 |
| 835 | 0x343 | ACC_CONTROL | 8 | 1 |
| 1556 | 0x614 | STEERING_LEVERS | 8 | 1 |
| 37 | 0x25 | STEER_ANGLE_SENSOR | 8 | 3 |
| 467 | 0x1d3 | PCM_CRUISE_2 | 8 | 4 |
| 921 | 0x399 | PCM_CRUISE_SM | 8 | 3 |
| 951 | 0x3b7 | ESP_CONTROL | 8 | 1 |
| 1042 | 0x412 | LKAS_HUD | 8 | 8 |
| 1553 | 0x611 | UI_SEETING | 8 | 1 |
| 1568 | 0x620 | SEATS_DOORS | 8 | 5 |
| 452 | 0x1c4 | POWERTRAIN | 8 | 2 |

## toyota_radar_dsu_tssp — Toyota TSS-P [B]

- Make: toyota; Radar/DSU bus
- Messages: 19; signals: 114
- Evidence: opendbc/opendbc/dbc/toyota_radar_dsu_tssp.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 768 | 0x300 | BUTTONS | 8 | 2 |
| 769 | 0x301 | OBJECT_0 | 8 | 6 |
| 771 | 0x303 | OBJECT_1 | 8 | 6 |
| 773 | 0x305 | OBJECT_2 | 8 | 6 |
| 775 | 0x307 | OBJECT_3 | 8 | 6 |
| 777 | 0x309 | OBJECT_4 | 8 | 6 |
| 779 | 0x30b | OBJECT_5 | 8 | 6 |
| 781 | 0x30d | OBJECT_6 | 8 | 6 |
| 783 | 0x30f | OBJECT_7 | 8 | 6 |
| 785 | 0x311 | OBJECT_8 | 8 | 6 |
| 787 | 0x313 | OBJECT_9 | 8 | 6 |
| 789 | 0x315 | OBJECT_10 | 8 | 6 |
| 791 | 0x317 | OBJECT_11 | 8 | 6 |
| 1664 | 0x680 | CLUSTER_F | 8 | 6 |
| 1665 | 0x681 | CLUSTER_F_A | 8 | 6 |
| 1666 | 0x682 | CLUSTER_L | 8 | 7 |
| 1667 | 0x683 | CLUSTER_R | 8 | 7 |
| 1668 | 0x684 | CLUSTER_L_A | 8 | 7 |
| 1669 | 0x685 | CLUSTER_R_A | 8 | 7 |

## toyota_tss2_adas — Toyota TSS 2.0 [B]

- Make: toyota; ADAS bus
- Messages: 35; signals: 183
- Evidence: opendbc/opendbc/dbc/toyota_tss2_adas.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 291 | 0x123 | STATUS_MSG | 7 | 3 |
| 384 | 0x180 | TRACK_A_0 | 8 | 7 |
| 385 | 0x181 | TRACK_A_1 | 8 | 7 |
| 386 | 0x182 | TRACK_A_2 | 8 | 7 |
| 387 | 0x183 | TRACK_A_3 | 8 | 7 |
| 388 | 0x184 | TRACK_A_4 | 8 | 7 |
| 389 | 0x185 | TRACK_A_5 | 8 | 7 |
| 390 | 0x186 | TRACK_A_6 | 8 | 7 |
| 391 | 0x187 | TRACK_A_7 | 8 | 7 |
| 392 | 0x188 | TRACK_A_8 | 8 | 7 |
| 393 | 0x189 | TRACK_A_9 | 8 | 7 |
| 394 | 0x18a | TRACK_A_10 | 8 | 7 |
| 395 | 0x18b | TRACK_A_11 | 8 | 7 |
| 396 | 0x18c | TRACK_A_12 | 8 | 7 |
| 397 | 0x18d | TRACK_A_13 | 8 | 7 |
| 398 | 0x18e | TRACK_A_14 | 8 | 7 |
| 399 | 0x18f | TRACK_A_15 | 8 | 7 |
| 400 | 0x190 | TRACK_B_0 | 8 | 4 |
| 401 | 0x191 | TRACK_B_1 | 8 | 4 |
| 402 | 0x192 | TRACK_B_2 | 8 | 4 |
| 403 | 0x193 | TRACK_B_3 | 8 | 4 |
| 404 | 0x194 | TRACK_B_4 | 8 | 4 |
| 405 | 0x195 | TRACK_B_5 | 8 | 4 |
| 406 | 0x196 | TRACK_B_6 | 8 | 4 |
| 407 | 0x197 | TRACK_B_7 | 8 | 4 |
| 408 | 0x198 | TRACK_B_8 | 8 | 4 |
| 409 | 0x199 | TRACK_B_9 | 8 | 4 |
| 410 | 0x19a | TRACK_B_10 | 8 | 4 |
| 411 | 0x19b | TRACK_B_11 | 8 | 4 |
| 412 | 0x19c | TRACK_B_12 | 8 | 4 |
| 413 | 0x19d | TRACK_B_13 | 8 | 4 |
| 414 | 0x19e | TRACK_B_14 | 8 | 4 |
| 415 | 0x19f | TRACK_B_15 | 8 | 4 |
| 576 | 0x240 | NEW_MSG_1 | 8 | 2 |
| 577 | 0x241 | NEW_MSG_2 | 8 | 2 |

## acura_ilx_2016_nidec — Acura ILX 2016 [B]

- Make: honda; Nidec powertrain DBC
- Messages: 36; signals: 69
- Evidence: opendbc/opendbc/dbc/acura_ilx_2016_nidec.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 768 | 0x300 | VEHICLE_STATE | 8 | 2 |
| 769 | 0x301 | VEHICLE_STATE2 | 8 | 2 |
| 1024 | 0x400 | RADAR_DIAGNOSTIC | 8 | 1 |
| 1040 | 0x410 | XXX_101 | 8 | 0 |
| 1041 | 0x411 | XXX_102 | 8 | 0 |
| 1042 | 0x412 | XXX_103 | 8 | 0 |
| 1043 | 0x413 | XXX_104 | 8 | 0 |
| 1044 | 0x414 | XXX_105 | 8 | 0 |
| 1045 | 0x415 | XXX_106 | 8 | 0 |
| 1046 | 0x416 | XXX_107 | 8 | 0 |
| 1047 | 0x417 | XXX_108 | 8 | 0 |
| 1056 | 0x420 | XXX_109 | 8 | 0 |
| 1057 | 0x421 | XXX_110 | 8 | 0 |
| 1058 | 0x422 | XXX_111 | 8 | 0 |
| 1059 | 0x423 | XXX_112 | 8 | 0 |
| 1060 | 0x424 | XXX_113 | 8 | 0 |
| 1072 | 0x430 | TRACK_0 | 8 | 4 |
| 1073 | 0x431 | TRACK_1 | 8 | 4 |
| 1074 | 0x432 | TRACK_2 | 8 | 4 |
| 1075 | 0x433 | TRACK_3 | 8 | 4 |
| 1076 | 0x434 | TRACK_4 | 8 | 4 |
| 1077 | 0x435 | TRACK_5 | 8 | 4 |
| 1078 | 0x436 | TRACK_6 | 8 | 4 |
| 1079 | 0x437 | TRACK_7 | 8 | 4 |
| 1080 | 0x438 | TRACK_8 | 8 | 4 |
| 1081 | 0x439 | TRACK_9 | 8 | 4 |
| 1088 | 0x440 | TRACK_10 | 8 | 4 |
| 1089 | 0x441 | TRACK_11 | 8 | 4 |
| 1090 | 0x442 | TRACK_12 | 8 | 4 |
| 1091 | 0x443 | TRACK_13 | 8 | 4 |
| 1092 | 0x444 | TRACK_14 | 8 | 4 |
| 1093 | 0x445 | TRACK_15 | 8 | 4 |
| 1279 | 0x4ff | XXX_114 | 8 | 0 |
| 1280 | 0x500 | XXX_115 | 8 | 0 |
| 1296 | 0x510 | XXX_116 | 8 | 0 |
| 1297 | 0x511 | XXX_117 | 8 | 0 |

## vw_mlb — VW MLB [B]

- Make: vw; Modular longitudinal platform (A4/A6/Q5...)
- Messages: 145; signals: 1438
- Evidence: opendbc/opendbc/dbc/vw_mlb.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 265 | 0x109 | ACC_01 | 8 | 11 |
| 780 | 0x30c | ACC_02 | 8 | 16 |
| 804 | 0x324 | ACC_04 | 8 | 11 |
| 269 | 0x10d | ACC_05 | 8 | 18 |
| 279 | 0x117 | ACC_10 | 8 | 22 |
| 64 | 0x40 | Airbag_01 | 8 | 25 |
| 1312 | 0x520 | Airbag_02 | 8 | 11 |
| 1633 | 0x661 | Anhaenger_01 | 3 | 14 |
| 777 | 0x309 | BEM_01 | 4 | 8 |
| 867 | 0x363 | Blinkmodi_01 | 4 | 23 |
| 482 | 0x1e2 | CCP_GE_CR0_01 | 8 | 1 |
| 490 | 0x1ea | CCP_GE_DTO_01 | 8 | 1 |
| 480 | 0x1e0 | CCP_MO_CRO_01 | 8 | 1 |
| 2616986624 | 0x9bfc0c00 | CCP_MO_CRO_02 | 8 | 1 |
| 488 | 0x1e8 | CCP_MO_DTO_01 | 8 | 1 |
| 2616986625 | 0x9bfc0c01 | CCP_MO_DTO_02 | 8 | 1 |
| 481 | 0x1e1 | CCP_MOS_CRO_01 | 8 | 1 |
| 2616986629 | 0x9bfc0c05 | CCP_MOS_CRO_02 | 8 | 1 |
| 489 | 0x1e9 | CCP_MOS_DTO_01 | 8 | 1 |
| 2616986630 | 0x9bfc0c06 | CCP_MOS_DTO_02 | 8 | 1 |
| 2617042432 | 0x9bfce600 | CCP_Soundaktor_CRO_01 | 8 | 1 |
| 2617042433 | 0x9bfce601 | CCP_Soundaktor_DTO_01 | 8 | 1 |
| 901 | 0x385 | Charisma_01 | 8 | 15 |
| 2617027072 | 0x9bfcaa00 | DEV_Airbag_01 | 4 | 1 |
| 1714 | 0x6b2 | Diagnose_01 | 8 | 10 |
| 1520 | 0x5f0 | Dimmung_01 | 5 | 4 |
| 1603 | 0x643 | Einheiten_01 | 3 | 9 |
| 260 | 0x104 | EPB_01 | 8 | 18 |
| 781 | 0x30d | EPB_02 | 4 | 7 |
| 256 | 0x100 | ESP_01 | 8 | 20 |
| 257 | 0x101 | ESP_02 | 8 | 16 |
| 259 | 0x103 | ESP_03 | 8 | 10 |
| 776 | 0x308 | ESP_04 | 8 | 19 |
| 262 | 0x106 | ESP_05 | 8 | 35 |
| 132 | 0x84 | ESP_06 | 8 | 10 |
| 914 | 0x392 | ESP_07_FR | 8 | 18 |
| 286 | 0x11e | ESP_08 | 8 | 13 |
| 1623 | 0x657 | ESP_17 | 8 | 3 |
| 924 | 0x39c | Gateway_05 | 8 | 44 |
| 927 | 0x39f | Gateway_06 | 8 | 1 |
| 1604 | 0x644 | Gateway_11 | 8 | 37 |
| 130 | 0x82 | Getriebe_01 | 8 | 12 |
| 131 | 0x83 | Getriebe_02 | 8 | 12 |
| 258 | 0x102 | Getriebe_03 | 8 | 12 |
| 1089 | 0x441 | Getriebe_04 | 8 | 13 |
| 294 | 0x126 | HCA_01 | 8 | 12 |
| 1811 | 0x713 | ISO_ABS_Req | 8 | 1 |
| 1917 | 0x77d | ISO_ABS_Resp | 8 | 1 |
| 1813 | 0x715 | ISO_Airbag_01_Req | 8 | 1 |
| 1919 | 0x77f | ISO_Airbag_01_Resp | 8 | 1 |
| 1874 | 0x752 | ISO_EPB_Req | 8 | 1 |
| 1980 | 0x7bc | ISO_EPB_Resp | 8 | 1 |
| 1795 | 0x703 | ISO_Funktionaler_Req_Aggregate | 8 | 1 |
| 1792 | 0x700 | ISO_Funktionaler_Req_All | 8 | 1 |
| 2015 | 0x7df | ISO_Funktionaler_Req_OBD | 8 | 1 |
| 2017 | 0x7e1 | ISO_Getriebe_01_Req | 8 | 1 |
| 2025 | 0x7e9 | ISO_Getriebe_01_Resp | 8 | 1 |
| 2016 | 0x7e0 | ISO_MO_01_Req | 8 | 1 |
| 2024 | 0x7e8 | ISO_MO_01_Resp | 8 | 1 |
| 2018 | 0x7e2 | ISO_MOS_01_Req | 8 | 1 |
| 2026 | 0x7ea | ISO_MOS_01_Resp | 8 | 1 |
| 2019 | 0x7e3 | ISO_OBD_reserv5_Req | 8 | 1 |
| 2027 | 0x7eb | ISO_OBD_reserv5_Resp | 8 | 1 |
| 1834 | 0x72a | ISO_SCR_Req | 8 | 1 |
| 1940 | 0x794 | ISO_SCR_Resp | 8 | 1 |
| 1814 | 0x716 | ISO_SCU_Req | 8 | 1 |
| 1920 | 0x780 | ISO_SCU_Resp | 8 | 1 |
| 1820 | 0x71c | ISO_Soundaktor_Req | 8 | 1 |
| 1926 | 0x786 | ISO_Soundaktor_Resp | 8 | 1 |
| 1875 | 0x753 | ISO_Waehlhebel_Req | 8 | 1 |
| 1981 | 0x7bd | ISO_Waehlhebel_Resp | 8 | 1 |
| 1424 | 0x590 | Kessy_02 | 8 | 31 |
| 960 | 0x3c0 | Klemmen_Status_01 | 4 | 7 |
| 959 | 0x3bf | Klima_01 | 8 | 23 |
| 779 | 0x30b | Kombi_01 | 8 | 27 |
| 1719 | 0x6b7 | Kombi_02 | 8 | 7 |
| 1720 | 0x6b8 | Kombi_03 | 8 | 4 |
| 517 | 0x205 | KS_Airbag | 8 | 1 |
| 640 | 0x280 | KS_Master | 8 | 1 |
| 919 | 0x397 | LDW_02 | 8 | 20 |
| 810 | 0x32a | LH_EPS_01 | 8 | 14 |
| 285 | 0x11d | LH_EPS_02 | 8 | 8 |
| 159 | 0x9f | LH_EPS_03 | 8 | 11 |
| 1137 | 0x471 | Licht_hinten_01 | 8 | 37 |
| 267 | 0x10b | LS_01 | 4 | 19 |
| 134 | 0x86 | LWI_01 | 8 | 11 |
| 128 | 0x80 | Motor_01 | 8 | 9 |
| 129 | 0x81 | Motor_02 | 8 | 14 |
| 261 | 0x105 | Motor_03 | 8 | 20 |
| 263 | 0x107 | Motor_04 | 8 | 8 |
| 782 | 0x30e | Motor_05 | 8 | 25 |
| 1088 | 0x440 | Motor_06 | 8 | 40 |
| 1600 | 0x640 | Motor_07 | 8 | 18 |
| 1607 | 0x647 | Motor_09 | 8 | 16 |
| 276 | 0x114 | Motor_10 | 8 | 10 |
| 1648 | 0x670 | Motor_18 | 8 | 5 |
| 1010 | 0x3f2 | Motor_19 | 8 | 7 |
| 1601 | 0x641 | Motor_Code_01 | 8 | 14 |
| 969 | 0x3c9 | MotorSlave_01 | 1 | 1 |
| 1696 | 0x6a0 | NightVision_01 | 8 | 9 |
| 1753 | 0x6d9 | NMH_EPB | 7 | 27 |
| 1728 | 0x6c0 | NMH_Gateway | 7 | 31 |
| 1730 | 0x6c2 | NMH_Getriebe | 7 | 28 |
| 1729 | 0x6c1 | NMH_Motor | 7 | 29 |
| 1736 | 0x6c8 | NMH_Motor_Slave | 7 | 16 |
| 1782 | 0x6f6 | NMH_SCR | 7 | 21 |
| 913 | 0x391 | OBD_01 | 8 | 10 |
| 803 | 0x323 | PCF_01 | 8 | 7 |
| 802 | 0x322 | PCR_01 | 8 | 6 |
| 929 | 0x3a1 | PSD_01 | 8 | 17 |
| 930 | 0x3a2 | PSD_02 | 8 | 59 |
| 2033 | 0x7f1 | Request_Airbag_Deployment | 8 | 1 |
| 2041 | 0x7f9 | Response_Airbag_Deployment | 8 | 1 |
| 1528 | 0x5f8 | SAK_01 | 8 | 4 |
| 1011 | 0x3f3 | SCR_01 | 8 | 5 |
| 1507 | 0x5e3 | SCR_02 | 8 | 9 |
| 1508 | 0x5e4 | SCR_03 | 8 | 14 |
| 1509 | 0x5e5 | SCR_04 | 8 | 7 |
| 1526 | 0x5f6 | SCR_05 | 8 | 8 |
| 1510 | 0x5e6 | SCR_CAL_ID1 | 8 | 8 |
| 1512 | 0x5e8 | SCR_CAL_ID2 | 8 | 8 |
| 133 | 0x85 | SCU_01 | 8 | 10 |
| 784 | 0x310 | SCU_02 | 8 | 5 |
| 1313 | 0x521 | STH_01 | 8 | 20 |
| 1172 | 0x494 | STS_01 | 8 | 18 |
| 783 | 0x30f | SWA_01 | 8 | 19 |
| 1413 | 0x585 | Systeminfo_01 | 8 | 17 |
| 1214 | 0x4be | TPD_SCU_01 | 8 | 1 |
| 768 | 0x300 | TPD_Tester_01 | 8 | 1 |
| 769 | 0x301 | TPD_Tester_02 | 8 | 1 |
| 770 | 0x302 | TPD_Tester_03 | 8 | 1 |
| 771 | 0x303 | TPD_Tester_04 | 8 | 1 |
| 772 | 0x304 | TPD_Tester_05 | 8 | 1 |
| 773 | 0x305 | TPD_Tester_06 | 8 | 1 |
| 774 | 0x306 | TPD_Tester_07 | 8 | 1 |
| 775 | 0x307 | TPD_Tester_08 | 8 | 1 |
| 542 | 0x21e | TPS_SCU | 7 | 1 |
| 512 | 0x200 | TPS_Tester | 7 | 1 |
| 268 | 0x10c | TSK_02 | 8 | 3 |
| 786 | 0x312 | TSK_03 | 8 | 6 |
| 270 | 0x10e | TSK_04 | 8 | 8 |
| 273 | 0x111 | TSK_05 | 8 | 13 |
| 1716 | 0x6b4 | VIN_01 | 8 | 21 |
| 1414 | 0x586 | Waehlhebel_02 | 8 | 1 |
| 1318 | 0x526 | BCM | 8 | 6 |

## vw_mqb — VW MQB [B]

- Make: vw; Modular transverse platform (Golf 7...)
- Messages: 113; signals: 1346
- Evidence: opendbc/opendbc/dbc/vw_mqb.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 290 | 0x122 | ACC_06 | 8 | 17 |
| 279 | 0x117 | ACC_10 | 8 | 23 |
| 304 | 0x130 | PLA_01 | 8 | 12 |
| 679 | 0x2a7 | ACC_13 | 8 | 12 |
| 681 | 0x2a9 | ACC_15 | 8 | 6 |
| 64 | 0x40 | Airbag_01 | 8 | 30 |
| 1312 | 0x520 | Airbag_02 | 8 | 11 |
| 65 | 0x41 | Airbag_03 | 8 | 3 |
| 1633 | 0x661 | Anhaenger_01 | 8 | 13 |
| 1626 | 0x65a | BCM_01 | 8 | 26 |
| 869 | 0x365 | BEM_05 | 8 | 11 |
| 1628 | 0x65c | BMS_Hybrid_01 | 8 | 12 |
| 901 | 0x385 | Charisma_01 | 8 | 16 |
| 945 | 0x3b1 | DC_Hybrid_01 | 8 | 9 |
| 1714 | 0x6b2 | Diagnose_01 | 8 | 10 |
| 1520 | 0x5f0 | Dimmung_01 | 8 | 5 |
| 1603 | 0x643 | Einheiten_01 | 8 | 9 |
| 260 | 0x104 | EPB_01 | 8 | 17 |
| 257 | 0x101 | ESP_02 | 8 | 16 |
| 262 | 0x106 | ESP_05 | 8 | 35 |
| 914 | 0x392 | ESP_07 | 8 | 18 |
| 278 | 0x116 | ESP_10 | 8 | 14 |
| 178 | 0xb2 | ESP_19 | 8 | 4 |
| 1629 | 0x65d | ESP_20 | 8 | 25 |
| 253 | 0xfd | ESP_21 | 8 | 27 |
| 987 | 0x3db | Gateway_72 | 8 | 31 |
| 989 | 0x3dd | Gateway_74 | 8 | 18 |
| 296 | 0x128 | Getriebe_06 | 3 | 6 |
| 173 | 0xad | Getriebe_11 | 8 | 15 |
| 174 | 0xae | Getriebe_12 | 8 | 12 |
| 301 | 0x12d | Getriebe_13 | 8 | 7 |
| 968 | 0x3c8 | Getriebe_14 | 8 | 12 |
| 158 | 0x9e | Getriebe_Hybrid_01 | 8 | 16 |
| 299 | 0x12b | GRA_ACC_01 | 8 | 16 |
| 960 | 0x3c0 | Klemmen_Status_01 | 4 | 6 |
| 949 | 0x3b5 | Klima_11 | 8 | 17 |
| 1625 | 0x659 | Klimakomp_01 | 8 | 10 |
| 2549088277 | 0x97f00015 | KN_Airbag_01 | 8 | 3 |
| 2549088380 | 0x97f0007c | KN_EMotor_01 | 8 | 3 |
| 2549088375 | 0x97f00077 | KN_Getriebe_01 | 8 | 3 |
| 2549088379 | 0x97f0007b | KN_Hybrid_01 | 8 | 3 |
| 2549088374 | 0x97f00076 | KN_MO_01 | 8 | 3 |
| 2549088284 | 0x97f0001c | KN_SAK | 8 | 3 |
| 779 | 0x30b | Kombi_01 | 8 | 28 |
| 1719 | 0x6b7 | Kombi_02 | 8 | 6 |
| 982 | 0x3d6 | Licht_hinten_01 | 8 | 37 |
| 134 | 0x86 | LWI_01 | 8 | 10 |
| 263 | 0x107 | Motor_04 | 8 | 8 |
| 1600 | 0x640 | Motor_07 | 8 | 18 |
| 1607 | 0x647 | Motor_09 | 8 | 12 |
| 167 | 0xa7 | Motor_11 | 8 | 10 |
| 168 | 0xa8 | Motor_12 | 8 | 8 |
| 958 | 0x3be | Motor_14 | 8 | 31 |
| 1631 | 0x65f | Motor_16 | 8 | 8 |
| 812 | 0x32c | Motor_17 | 8 | 9 |
| 1648 | 0x670 | Motor_18 | 8 | 7 |
| 289 | 0x121 | Motor_20 | 8 | 15 |
| 967 | 0x3c7 | Motor_26 | 8 | 33 |
| 1601 | 0x641 | Motor_Code_01 | 8 | 17 |
| 157 | 0x9d | Motor_Hybrid_01 | 8 | 11 |
| 811 | 0x32b | Motor_Hybrid_02 | 8 | 3 |
| 2600468501 | 0x9b000015 | NMH_Airbag_01 | 8 | 8 |
| 2600468604 | 0x9b00007c | NMH_EMotor_01 | 8 | 9 |
| 2600468496 | 0x9b000010 | NMH_Gateway | 8 | 21 |
| 2600468599 | 0x9b000077 | NMH_Getriebe_01 | 8 | 12 |
| 2600468603 | 0x9b00007b | NMH_Hybrid_01 | 8 | 10 |
| 2600468598 | 0x9b000076 | NMH_MO_01 | 8 | 16 |
| 913 | 0x391 | OBD_01 | 8 | 10 |
| 1630 | 0x65e | OBD_Tankgeber_01 | 8 | 8 |
| 1437 | 0x59d | Remotestart_FFB | 8 | 3 |
| 984 | 0x3d8 | RGS_VL_01 | 8 | 11 |
| 1528 | 0x5f8 | SAK_01 | 8 | 2 |
| 1313 | 0x521 | STH_01 | 8 | 20 |
| 1172 | 0x494 | STS_01 | 8 | 17 |
| 1413 | 0x585 | Systeminfo_01 | 8 | 23 |
| 288 | 0x120 | TSK_06 | 8 | 15 |
| 798 | 0x31e | TSK_07 | 8 | 12 |
| 346 | 0x15a | TSK_08 | 8 | 12 |
| 1716 | 0x6b4 | VIN_01 | 8 | 21 |
| 175 | 0xaf | Waehlhebel_03 | 4 | 8 |
| 916 | 0x394 | WBA_03 | 8 | 9 |
| 1602 | 0x642 | WIV_01 | 8 | 6 |
| 294 | 0x126 | HCA_01 | 8 | 12 |
| 810 | 0x32a | LH_EPS_01 | 8 | 15 |
| 159 | 0x9f | LH_EPS_03 | 8 | 12 |
| 286 | 0x11e | ESP_08 | 8 | 13 |
| 919 | 0x397 | LDW_02 | 8 | 20 |
| 780 | 0x30c | ACC_02 | 8 | 18 |
| 302 | 0x12e | ACC_07 | 8 | 11 |
| 264 | 0x108 | Fahrwerk_01 | 8 | 2 |
| 695 | 0x2b7 | RCTA_01 | 8 | 2 |
| 783 | 0x30f | SWA_01 | 8 | 26 |
| 804 | 0x324 | ACC_04 | 8 | 14 |
| 917 | 0x395 | LWR_AFS_01 | 8 | 0 |
| 991 | 0x3df | Gateway_76 | 8 | 0 |
| 997 | 0x3e5 | TSG_FT_02 | 8 | 2 |
| 1175 | 0x497 | Parkhilfe_01 | 8 | 0 |
| 427 | 0x1ab | ESP_33 | 8 | 41 |
| 418 | 0x1a2 | ESP_15 | 8 | 2 |
| 1122 | 0x462 | PSD_04 | 8 | 1 |
| 1123 | 0x463 | PSD_05 | 8 | 2 |
| 1124 | 0x464 | PSD_06 | 8 | 0 |
| 988 | 0x3dc | Gateway_73 | 8 | 4 |
| 792 | 0x318 | Kamera_Status | 8 | 0 |
| 981 | 0x3d5 | Licht_Anf_01 | 8 | 27 |
| 1440 | 0x5a0 | RLS_01 | 8 | 0 |
| 870 | 0x366 | Blinkmodi_02 | 8 | 8 |
| 1385 | 0x569 | HVEM_04 | 8 | 0 |
| 1605 | 0x645 | FLA_01 | 8 | 0 |
| 1624 | 0x658 | Licht_vorne_01 | 8 | 0 |
| 1646 | 0x66e | Klima_03 | 8 | 0 |
| 1720 | 0x6b8 | Kombi_03 | 8 | 10 |
| 391 | 0x187 | Motor_EV_01 | 8 | 15 |

## vw_mqbevo — VW MQB-Evo [B]

- Make: vw; Golf 8 / Octavia 4 platform
- Messages: 136; signals: 1197
- Evidence: opendbc/opendbc/dbc/vw_mqbevo.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 64 | 0x40 | Airbag_01 | 8 | 24 |
| 65 | 0x41 | Airbag_03 | 8 | 3 |
| 134 | 0x86 | LWI_01 | 8 | 10 |
| 157 | 0x9d | Motor_Hybrid_01 | 8 | 11 |
| 158 | 0x9e | Getriebe_Hybrid_01 | 8 | 16 |
| 159 | 0x9f | LH_EPS_03 | 8 | 11 |
| 167 | 0xa7 | Motor_11 | 8 | 10 |
| 168 | 0xa8 | Motor_12 | 8 | 8 |
| 173 | 0xad | Getriebe_11 | 8 | 12 |
| 174 | 0xae | Getriebe_12 | 8 | 12 |
| 175 | 0xaf | Waehlhebel_03 | 4 | 8 |
| 178 | 0xb2 | ESP_19 | 8 | 4 |
| 252 | 0xfc | ESP_NEW_1 | 48 | 6 |
| 253 | 0xfd | ESP_21 | 8 | 18 |
| 257 | 0x101 | ESP_02 | 8 | 16 |
| 258 | 0x102 | ESP_NEW_2 | 48 | 4 |
| 260 | 0x104 | EPB_01 | 8 | 17 |
| 262 | 0x106 | ESP_05 | 8 | 35 |
| 263 | 0x107 | Motor_04 | 8 | 8 |
| 264 | 0x108 | Fahrwerk_01 | 8 | 2 |
| 267 | 0x10b | MOTOR_NEW_1 | 32 | 4 |
| 278 | 0x116 | ESP_10 | 8 | 14 |
| 279 | 0x117 | ACC_10 | 8 | 22 |
| 286 | 0x11e | VehicleSpeed | 8 | 3 |
| 288 | 0x120 | TSK_06 | 8 | 11 |
| 289 | 0x121 | Motor_20 | 8 | 11 |
| 290 | 0x122 | ACC_06 | 8 | 17 |
| 294 | 0x126 | HCA_01 | 8 | 12 |
| 296 | 0x128 | Getriebe_06 | 3 | 6 |
| 299 | 0x12b | GRA_ACC_01 | 8 | 17 |
| 301 | 0x12d | Getriebe_13 | 8 | 7 |
| 302 | 0x12e | ACC_07 | 8 | 11 |
| 313 | 0x139 | ESP_NEW_3 | 32 | 6 |
| 317 | 0x13d | MOTOR_NEW_2 | 32 | 4 |
| 333 | 0x14d | ACC_NEW_1 | 32 | 3 |
| 387 | 0x183 | CAMERA_NEW_3_HF | 64 | 1 |
| 391 | 0x187 | EV_Gearshift | 8 | 4 |
| 418 | 0x1a2 | ESP_15 | 8 | 2 |
| 420 | 0x1a4 | CAMERA_NEW_11 | 8 | 0 |
| 427 | 0x1ab | ESP_33 | 8 | 2 |
| 496 | 0x1f0 | CAMERA_NEW_10 | 8 | 0 |
| 519 | 0x207 | CAMERA_NEW_1_HF | 64 | 2 |
| 564 | 0x234 | CAMERA_NEW_2_HF | 64 | 0 |
| 589 | 0x24d | NEW_MSG_24D | 64 | 1 |
| 619 | 0x26b | CAMERA_NEW_5 | 8 | 0 |
| 679 | 0x2a7 | ACC_13 | 8 | 11 |
| 681 | 0x2a9 | ACC_15 | 8 | 6 |
| 695 | 0x2b7 | RCTA_01 | 8 | 2 |
| 768 | 0x300 | ACC_NEW_2 | 48 | 3 |
| 771 | 0x303 | HCA_NEW | 24 | 5 |
| 779 | 0x30b | Kombi_01 | 8 | 28 |
| 780 | 0x30c | ACC_02 | 8 | 18 |
| 783 | 0x30f | SWA_01 | 8 | 19 |
| 792 | 0x318 | Kamera_Status | 8 | 0 |
| 798 | 0x31e | TSK_07 | 8 | 6 |
| 804 | 0x324 | ACC_04 | 8 | 14 |
| 811 | 0x32b | Motor_Hybrid_02 | 8 | 3 |
| 812 | 0x32c | Motor_17 | 8 | 9 |
| 869 | 0x365 | BEM_05 | 8 | 11 |
| 870 | 0x366 | Blinkmodi_02 | 8 | 8 |
| 873 | 0x369 | CAMERA_NEW_4 | 8 | 0 |
| 901 | 0x385 | Charisma_01 | 8 | 16 |
| 913 | 0x391 | OBD_01 | 8 | 10 |
| 914 | 0x392 | ESP_07 | 8 | 18 |
| 916 | 0x394 | WBA_03 | 8 | 9 |
| 917 | 0x395 | LWR_AFS_01 | 8 | 0 |
| 919 | 0x397 | LDW_02 | 8 | 20 |
| 945 | 0x3b1 | DC_Hybrid_01 | 8 | 9 |
| 949 | 0x3b5 | Klima_11 | 8 | 17 |
| 958 | 0x3be | Motor_14 | 8 | 31 |
| 960 | 0x3c0 | Klemmen_Status_01 | 4 | 6 |
| 967 | 0x3c7 | Motor_26 | 8 | 33 |
| 968 | 0x3c8 | Getriebe_14 | 8 | 12 |
| 981 | 0x3d5 | Licht_Anf_01 | 8 | 0 |
| 982 | 0x3d6 | Licht_hinten_01 | 8 | 37 |
| 984 | 0x3d8 | RGS_VL_01 | 8 | 11 |
| 987 | 0x3db | Gateway_72 | 8 | 31 |
| 988 | 0x3dc | Gateway_73 | 8 | 0 |
| 989 | 0x3dd | Gateway_74 | 8 | 18 |
| 991 | 0x3df | Gateway_76 | 8 | 0 |
| 997 | 0x3e5 | TSG_FT_02 | 8 | 2 |
| 1122 | 0x462 | PSD_04 | 8 | 1 |
| 1123 | 0x463 | PSD_05 | 8 | 2 |
| 1124 | 0x464 | PSD_06 | 8 | 0 |
| 1172 | 0x494 | STS_01 | 8 | 17 |
| 1175 | 0x497 | Parkhilfe_01 | 8 | 0 |
| 1312 | 0x520 | Airbag_02 | 8 | 11 |
| 1313 | 0x521 | STH_01 | 8 | 20 |
| 1385 | 0x569 | HVEM_04 | 8 | 0 |
| 1413 | 0x585 | Systeminfo_01 | 8 | 23 |
| 1437 | 0x59d | Remotestart_FFB | 8 | 3 |
| 1440 | 0x5a0 | RLS_01 | 8 | 0 |
| 1520 | 0x5f0 | Dimmung_01 | 8 | 5 |
| 1528 | 0x5f8 | SAK_01 | 8 | 2 |
| 1600 | 0x640 | Motor_07 | 8 | 18 |
| 1601 | 0x641 | Motor_Code_01 | 8 | 17 |
| 1602 | 0x642 | WIV_01 | 8 | 6 |
| 1603 | 0x643 | Einheiten_01 | 8 | 9 |
| 1605 | 0x645 | FLA_01 | 8 | 0 |
| 1607 | 0x647 | Motor_09 | 8 | 12 |
| 1624 | 0x658 | Licht_vorne_01 | 8 | 0 |
| 1625 | 0x659 | Klimakomp_01 | 8 | 10 |
| 1626 | 0x65a | BCM_01 | 8 | 26 |
| 1628 | 0x65c | BMS_Hybrid_01 | 8 | 12 |
| 1629 | 0x65d | ESP_20 | 8 | 8 |
| 1630 | 0x65e | OBD_Tankgeber_01 | 8 | 8 |
| 1631 | 0x65f | Motor_16 | 8 | 8 |
| 1633 | 0x661 | Anhaenger_01 | 8 | 13 |
| 1646 | 0x66e | Klima_03 | 8 | 0 |
| 1648 | 0x670 | Motor_18 | 8 | 7 |
| 1714 | 0x6b2 | Diagnose_01 | 8 | 10 |
| 1716 | 0x6b4 | VIN_01 | 8 | 21 |
| 1719 | 0x6b7 | Kombi_02 | 8 | 6 |
| 1720 | 0x6b8 | Kombi_03 | 8 | 10 |
| 316495015 | 0x12dd54a7 | CAMERA_NEW_6 | 32 | 0 |
| 380196019 | 0x16a954b3 | CAMERA_NEW_16 | 16 | 0 |
| 380196036 | 0x16a954c4 | CAMERA_NEW_18 | 8 | 0 |
| 389224720 | 0x17331910 | CAMERA_NEW_13 | 3 | 0 |
| 389226768 | 0x17332110 | CAMERA_NEW_12 | 2 | 0 |
| 389241616 | 0x17335b10 | CAMERA_NEW_14 | 5 | 0 |
| 401604687 | 0x17f0004f | CAMERA_NEW_9 | 8 | 0 |
| 441800082 | 0x1a555592 | CAMERA_NEW_15 | 8 | 0 |
| 441800100 | 0x1a5555a4 | CAMERA_NEW_8 | 64 | 0 |
| 441800101 | 0x1a5555a5 | CAMERA_NEW_7 | 64 | 0 |
| 2549088277 | 0x97f00015 | KN_Airbag_01 | 8 | 3 |
| 2549088284 | 0x97f0001c | KN_SAK | 8 | 3 |
| 2549088374 | 0x97f00076 | KN_MO_01 | 8 | 3 |
| 2549088375 | 0x97f00077 | KN_Getriebe_01 | 8 | 3 |
| 2549088379 | 0x97f0007b | KN_Hybrid_01 | 8 | 3 |
| 2549088380 | 0x97f0007c | KN_EMotor_01 | 8 | 3 |
| 2600468496 | 0x9b000010 | NMH_Gateway | 8 | 21 |
| 2600468501 | 0x9b000015 | NMH_Airbag_01 | 8 | 8 |
| 2600468598 | 0x9b000076 | NMH_MO_01 | 8 | 16 |
| 2600468599 | 0x9b000077 | NMH_Getriebe_01 | 8 | 12 |
| 2600468603 | 0x9b00007b | NMH_Hybrid_01 | 8 | 10 |
| 2600468604 | 0x9b00007c | NMH_EMotor_01 | 8 | 9 |

## vw_pq — VW PQ [B]

- Make: vw; Older PQ platform (Golf 5/6...)
- Messages: 86; signals: 1321
- Evidence: opendbc/opendbc/dbc/vw_pq.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 1394 | 0x572 | ZAS_1 | 2 | 10 |
| 1336 | 0x538 | Wischer_1 | 2 | 14 |
| 1464 | 0x5b8 | WFS_1 | 2 | 3 |
| 1096 | 0x448 | Waehlhebel_1 | 4 | 8 |
| 1496 | 0x5d8 | Verbauliste_1 | 8 | 59 |
| 1488 | 0x5d0 | Systeminfo_1 | 6 | 20 |
| 268 | 0x10c | Slave_1 | 8 | 13 |
| 1332 | 0x534 | Sitz_info | 2 | 6 |
| 1810 | 0x712 | PSG_3 | 2 | 1 |
| 1298 | 0x512 | PSG_2 | 8 | 4 |
| 274 | 0x112 | PSG_1 | 8 | 6 |
| 1300 | 0x514 | NOX_1 | 8 | 13 |
| 1424 | 0x590 | Niveau_1 | 6 | 25 |
| 1328 | 0x530 | Navigation_1 | 7 | 12 |
| 1792 | 0x700 | MSG_3 | 3 | 2 |
| 1280 | 0x500 | MSG_2 | 8 | 4 |
| 256 | 0x100 | MSG_1 | 8 | 5 |
| 1796 | 0x704 | Motor_NOX | 8 | 7 |
| 900 | 0x384 | Motor_Momente | 8 | 1 |
| 1408 | 0x580 | Motor_Flexia | 8 | 20 |
| 1416 | 0x588 | Motor_7 | 8 | 13 |
| 1160 | 0x488 | Motor_6 | 8 | 11 |
| 1152 | 0x480 | Motor_5 | 8 | 36 |
| 896 | 0x380 | Motor_3 | 8 | 17 |
| 648 | 0x288 | Motor_2 | 8 | 21 |
| 640 | 0x280 | Motor_1 | 8 | 13 |
| 262 | 0x106 | Master_3 | 8 | 5 |
| 260 | 0x104 | Master_2 | 8 | 9 |
| 258 | 0x102 | Master_1 | 8 | 9 |
| 1984 | 0x7c0 | LWS_Kalibrierung | 2 | 4 |
| 1986 | 0x7c2 | Lenkwinkel_Init | 4 | 2 |
| 192 | 0xc0 | Lenkwinkel_1__RB_ | 2 | 7 |
| 196 | 0xc4 | Lenkwinkel_1__ITT_ | 2 | 7 |
| 194 | 0xc2 | Lenkwinkel_1 | 8 | 11 |
| 1502 | 0x5de | Lenkhilfe_Fehler | 7 | 39 |
| 976 | 0x3d0 | Lenkhilfe_1 | 2 | 22 |
| 1312 | 0x520 | Kombi_3 | 8 | 24 |
| 1056 | 0x420 | Kombi_2 | 8 | 15 |
| 800 | 0x320 | Kombi_1 | 8 | 24 |
| 1504 | 0x5e0 | Klima_1 | 8 | 18 |
| 906 | 0x38a | GRA_Neu | 4 | 20 |
| 904 | 0x388 | GRA | 3 | 10 |
| 1352 | 0x548 | Getriebe_4 | 3 | 7 |
| 1344 | 0x540 | Getriebe_2 | 8 | 20 |
| 1088 | 0x440 | Getriebe_1 | 8 | 20 |
| 912 | 0x390 | Gate_Komf_1 | 8 | 54 |
| 1340 | 0x53c | Fahrwerk_1 | 1 | 4 |
| 1472 | 0x5c0 | EPB_1 | 8 | 30 |
| 1326 | 0x52e | Diag_Lenkhilfe | 3 | 5 |
| 1432 | 0x598 | Daempfer_1 | 2 | 8 |
| 1392 | 0x570 | BSG_Last | 4 | 21 |
| 1136 | 0x470 | BSG_Kombi | 5 | 25 |
| 424 | 0x1a8 | Bremse_6 | 3 | 5 |
| 1192 | 0x4a8 | Bremse_5 | 8 | 27 |
| 672 | 0x2a0 | Bremse_4 | 3 | 4 |
| 1184 | 0x4a0 | Bremse_3 | 8 | 8 |
| 1440 | 0x5a0 | Bremse_2 | 8 | 13 |
| 416 | 0x1a0 | Bremse_1 | 8 | 25 |
| 680 | 0x2a8 | Bremsbooster_1 | 3 | 11 |
| 1400 | 0x578 | BatMan_1 | 1 | 7 |
| 704 | 0x2c0 | Allrad_1 | 5 | 17 |
| 1360 | 0x550 | Airbag_2 | 2 | 7 |
| 80 | 0x50 | Airbag_1 | 4 | 20 |
| 864 | 0x360 | ADR_System | 8 | 27 |
| 608 | 0x260 | ADR_2 | 4 | 7 |
| 1324 | 0x52c | ADR_1 | 8 | 22 |
| 1550 | 0x60e | Einheiten_1 | 2 | 1 |
| 872 | 0x368 | ACC_System | 8 | 14 |
| 1386 | 0x56a | ACC_GRA_Anzeige | 8 | 19 |
| 208 | 0xd0 | Lenkhilfe_3 | 6 | 11 |
| 978 | 0x3d2 | Lenkhilfe_2 | 7 | 11 |
| 980 | 0x3d4 | PLA_1 | 8 | 8 |
| 210 | 0xd2 | HCA_1 | 5 | 7 |
| 644 | 0x284 | Motor_Bremse | 6 | 9 |
| 870 | 0x366 | AWV | 8 | 31 |
| 1470 | 0x5be | LDW_Status | 8 | 15 |
| 428 | 0x1ac | Bremse_8 | 8 | 22 |
| 928 | 0x3a0 | Bremse_10 | 8 | 18 |
| 835 | 0x343 | RDK_Status | 3 | 20 |
| 914 | 0x392 | Gate_Komf_2 | 8 | 34 |
| 954 | 0x3ba | SWA_1 | 8 | 9 |
| 1175 | 0x497 | Parkhilfe_01 | 8 | 23 |
| 1463 | 0x5b7 | Bremse_11 | 8 | 10 |
| 1500 | 0x5dc | Soll_Verbauliste_neu | 8 | 64 |
| 1490 | 0x5d2 | Ident | 8 | 21 |
| 2000 | 0x7d0 | Diagnose_1 | 8 | 10 |

## hyundai_2015_ccan — Hyundai 2015 [B]

- Make: hyundai; Chassis CAN
- Messages: 113; signals: 1152
- Evidence: opendbc/opendbc/dbc/hyundai_2015_ccan.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 1532 | 0x5fc | ODS13 | 5 | 5 |
| 1531 | 0x5fb | ODS12 | 8 | 8 |
| 1530 | 0x5fa | ODS11 | 8 | 10 |
| 1017 | 0x3f9 | ECS12 | 4 | 4 |
| 1268 | 0x4f4 | SPAS12 | 8 | 23 |
| 1265 | 0x4f1 | CLU11 | 4 | 12 |
| 1492 | 0x5d4 | TMU_GW_PE_01 | 8 | 2 |
| 1491 | 0x5d3 | HU_DATC_PE_00 | 8 | 3 |
| 1490 | 0x5d2 | HU_DATC_E_02 | 8 | 2 |
| 1479 | 0x5c7 | EMS21 | 8 | 8 |
| 1472 | 0x5c0 | GW_Warning_PE | 8 | 7 |
| 1984 | 0x7c0 | CAL_SAS11 | 2 | 2 |
| 1456 | 0x5b0 | CLU12 | 4 | 1 |
| 688 | 0x2b0 | SAS11 | 5 | 5 |
| 1441 | 0x5a1 | ACU12 | 8 | 1 |
| 1440 | 0x5a0 | ACU11 | 8 | 14 |
| 1437 | 0x59d | AHLS11 | 8 | 2 |
| 1434 | 0x59a | PSB11 | 2 | 6 |
| 916 | 0x394 | TCS13 | 8 | 21 |
| 1427 | 0x593 | TPMS11 | 6 | 12 |
| 915 | 0x393 | TCS12 | 4 | 3 |
| 1170 | 0x492 | EMS19 | 8 | 13 |
| 1425 | 0x591 | AFLS11 | 2 | 3 |
| 912 | 0x390 | SPAS11 | 7 | 8 |
| 1168 | 0x490 | EPB11 | 7 | 14 |
| 399 | 0x18f | EMS_H12 | 8 | 21 |
| 1419 | 0x58b | LCA11 | 8 | 18 |
| 906 | 0x38a | ABS11 | 8 | 7 |
| 903 | 0x387 | WHL_PUL11 | 6 | 9 |
| 1415 | 0x587 | TMU11 | 8 | 8 |
| 902 | 0x386 | WHL_SPD11 | 8 | 8 |
| 1414 | 0x586 | EVP11 | 3 | 1 |
| 1412 | 0x584 | AAF11 | 8 | 9 |
| 900 | 0x384 | EMS17 | 8 | 10 |
| 387 | 0x183 | REA11 | 8 | 17 |
| 1411 | 0x583 | CUBIS11 | 8 | 1 |
| 899 | 0x383 | FATC11 | 8 | 19 |
| 129 | 0x81 | EMS_DCT12 | 8 | 6 |
| 897 | 0x381 | MDPS11 | 8 | 13 |
| 896 | 0x380 | DI_BOX13 | 8 | 12 |
| 640 | 0x280 | EMS13 | 8 | 13 |
| 128 | 0x80 | EMS_DCT11 | 8 | 10 |
| 1407 | 0x57f | HU_MON_PE_01 | 8 | 1 |
| 127 | 0x7f | CGW5 | 8 | 25 |
| 1151 | 0x47f | ESP11 | 6 | 11 |
| 1397 | 0x575 | HU_AVM_E_00 | 8 | 13 |
| 1395 | 0x573 | HU_AVM_E_01 | 8 | 4 |
| 1393 | 0x571 | OPI11 | 5 | 9 |
| 625 | 0x271 | LPI11 | 8 | 13 |
| 356 | 0x164 | VSM11 | 4 | 6 |
| 1379 | 0x563 | PGS_HU_PE_01 | 8 | 4 |
| 354 | 0x162 | TCU_DCT13 | 3 | 3 |
| 1378 | 0x562 | HUD11 | 4 | 3 |
| 608 | 0x260 | EMS16 | 8 | 15 |
| 1371 | 0x55b | AVM_HU_PE_00 | 8 | 12 |
| 1370 | 0x55a | HU_AVM_PE_00 | 8 | 1 |
| 1369 | 0x559 | CGW4 | 8 | 23 |
| 1367 | 0x557 | EngFrzFrm12 | 8 | 6 |
| 1366 | 0x556 | EngFrzFrm11 | 8 | 6 |
| 1365 | 0x555 | FPCM11 | 8 | 9 |
| 852 | 0x354 | LVR11 | 7 | 12 |
| 1363 | 0x553 | CGW2 | 8 | 41 |
| 339 | 0x153 | TCS11 | 8 | 29 |
| 1362 | 0x552 | SNV11 | 4 | 6 |
| 593 | 0x251 | MDPS12 | 8 | 11 |
| 1360 | 0x550 | IAP11 | 3 | 3 |
| 1356 | 0x54c | TCU_DCT14 | 8 | 2 |
| 1353 | 0x549 | BAT11 | 8 | 9 |
| 1351 | 0x547 | EMS15 | 8 | 12 |
| 1350 | 0x546 | DI_BOX12 | 8 | 11 |
| 1349 | 0x545 | EMS14 | 8 | 8 |
| 68 | 0x44 | DATC11 | 8 | 6 |
| 67 | 0x43 | DATC13 | 8 | 24 |
| 66 | 0x42 | DATC12 | 8 | 7 |
| 1345 | 0x541 | CGW1 | 8 | 43 |
| 64 | 0x40 | DATC14 | 8 | 9 |
| 832 | 0x340 | LKAS11 | 8 | 19 |
| 1342 | 0x53e | LKAS12 | 6 | 5 |
| 1338 | 0x53a | TMU_GW_E_01 | 8 | 5 |
| 1078 | 0x436 | PAS11 | 4 | 12 |
| 48 | 0x30 | EMS18 | 6 | 5 |
| 1322 | 0x52a | CLU15 | 8 | 15 |
| 1066 | 0x42a | _4WD13 | 6 | 4 |
| 1065 | 0x429 | _4WD12 | 8 | 6 |
| 809 | 0x329 | EMS12 | 8 | 18 |
| 1064 | 0x428 | _4WD11 | 8 | 12 |
| 1319 | 0x527 | HU_GW_E_01 | 8 | 12 |
| 1318 | 0x526 | HU_GW_E_00 | 8 | 9 |
| 1317 | 0x525 | GW_HU_E_01 | 8 | 10 |
| 1316 | 0x524 | GW_HU_E_00 | 8 | 8 |
| 1315 | 0x523 | GW_SWRC_PE | 8 | 12 |
| 1314 | 0x522 | GW_IPM_PE_1 | 8 | 10 |
| 1057 | 0x421 | SCC12 | 8 | 21 |
| 1313 | 0x521 | GW_DDM_PE | 8 | 6 |
| 1056 | 0x420 | SCC11 | 8 | 15 |
| 1312 | 0x520 | CGW3 | 8 | 4 |
| 544 | 0x220 | ESP12 | 8 | 14 |
| 1307 | 0x51b | CLU16 | 8 | 3 |
| 790 | 0x316 | EMS11 | 8 | 13 |
| 1301 | 0x515 | CLU14 | 8 | 26 |
| 275 | 0x113 | TCU13 | 8 | 18 |
| 274 | 0x112 | TCU12 | 8 | 12 |
| 273 | 0x111 | TCU11 | 8 | 13 |
| 16 | 0x10 | ACU13 | 8 | 1 |
| 1040 | 0x410 | CGW_USM1 | 8 | 17 |
| 1292 | 0x50c | CLU13 | 8 | 17 |
| 1290 | 0x50a | SCC13 | 8 | 3 |
| 1287 | 0x507 | TCS15 | 4 | 11 |
| 1282 | 0x502 | TCU14 | 4 | 7 |
| 1281 | 0x501 | ECS11 | 3 | 14 |
| 1024 | 0x400 | CLU_CFG11 | 2 | 1 |
| 1280 | 0x500 | ACU14 | 1 | 3 |
| 512 | 0x200 | EMS20 | 6 | 3 |

## hyundai_2015_mcan — Hyundai 2015 [B]

- Make: hyundai; Multimedia CAN
- Messages: 171; signals: 1184
- Evidence: opendbc/opendbc/dbc/hyundai_2015_mcan.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 3221225472 | 0xc0000000 | VECTOR__INDEPENDENT_SIG_MSG | 0 | 4 |
| 2046 | 0x7fe | TP_EDT_AMP | 8 | 8 |
| 251 | 0xfb | HU_TMU_E_02 | 8 | 6 |
| 250 | 0xfa | HU_TMU_E_01 | 8 | 7 |
| 1269 | 0x4f5 | TP_CLU_ANDAUTO_HU | 8 | 8 |
| 1268 | 0x4f4 | TP_HU_ANDAUTO_CLU | 8 | 8 |
| 1267 | 0x4f3 | TP_CLU_CARPLAY_HU | 8 | 8 |
| 1266 | 0x4f2 | TP_HU_CARPLAY_CLU | 8 | 8 |
| 1263 | 0x4ef | TP_CLU_IBOX_HU | 8 | 8 |
| 1262 | 0x4ee | TP_HU_IBOX_CLU | 8 | 8 |
| 1261 | 0x4ed | TP_CLU_DLNA_HU | 8 | 8 |
| 1260 | 0x4ec | TP_HU_DLNA_CLU | 8 | 8 |
| 491 | 0x1eb | GW_DDM_PE | 8 | 6 |
| 1259 | 0x4eb | TP_CLU_MP_HU | 8 | 8 |
| 1258 | 0x4ea | TP_HU_MP_CLU | 8 | 8 |
| 1257 | 0x4e9 | TP_CLU_FM_HU | 8 | 8 |
| 1256 | 0x4e8 | TP_HU_FM_CLU | 8 | 8 |
| 1255 | 0x4e7 | TP_CLU_MLT_HU | 8 | 8 |
| 487 | 0x1e7 | HU_CLU_PE_13 | 8 | 9 |
| 1254 | 0x4e6 | TP_HU_MLT_CLU | 8 | 8 |
| 486 | 0x1e6 | HU_CLU_PE_12 | 8 | 7 |
| 229 | 0xe5 | HU_SYS_E_00 | 8 | 6 |
| 1253 | 0x4e5 | TP_CLU_VCDC_HU | 8 | 8 |
| 485 | 0x1e5 | HU_CLU_PE_11 | 8 | 13 |
| 1252 | 0x4e4 | TP_HU_VCDC_CLU | 8 | 8 |
| 1251 | 0x4e3 | TP_CLU_JB_HU | 8 | 8 |
| 1250 | 0x4e2 | TP_HU_JB_CLU | 8 | 8 |
| 1248 | 0x4e0 | TP_TMU_HU | 8 | 8 |
| 479 | 0x1df | CLU_HU_PE_01 | 8 | 13 |
| 2015 | 0x7df | TP_EDT_All_Req | 8 | 8 |
| 474 | 0x1da | CLU_HU_PE_02 | 8 | 6 |
| 1495 | 0x5d7 | CLU_HU_P_05 | 8 | 6 |
| 1494 | 0x5d6 | CLU_HU_P_01 | 8 | 2 |
| 214 | 0xd6 | AMP_HU_E_SYS | 8 | 8 |
| 1492 | 0x5d4 | CLU_HU_P_04 | 8 | 5 |
| 1491 | 0x5d3 | CLU_HU_P_03 | 8 | 5 |
| 1490 | 0x5d2 | CLU_HU_P_02 | 8 | 3 |
| 1489 | 0x5d1 | DATC_P_B_01 | 8 | 4 |
| 465 | 0x1d1 | CLU_HU_PE_03 | 8 | 4 |
| 1232 | 0x4d0 | TP_HU_TMU | 8 | 8 |
| 1488 | 0x5d0 | CLU_HU_P_00 | 8 | 6 |
| 208 | 0xd0 | CLU_HU_E_SYS | 8 | 6 |
| 448 | 0x1c0 | HU_DATC_PE_00 | 8 | 7 |
| 1211 | 0x4bb | TP_HU_TBT_CLU | 8 | 8 |
| 1207 | 0x4b7 | TP_HU_DAB_CLU | 8 | 8 |
| 1206 | 0x4b6 | TP_HU_XM_CLU | 8 | 8 |
| 1204 | 0x4b4 | TP_HU_DMB_CLU | 8 | 8 |
| 432 | 0x1b0 | TMU_GW_PE_01 | 8 | 5 |
| 1195 | 0x4ab | TP_CLU_TBT_HU | 8 | 8 |
| 1191 | 0x4a7 | TP_CLU_DAB_HU | 8 | 8 |
| 1190 | 0x4a6 | TP_CLU_XM_HU | 8 | 8 |
| 1188 | 0x4a4 | TP_CLU_DMB_HU | 8 | 8 |
| 1179 | 0x49b | TP_HU_NAVI_CLU | 8 | 8 |
| 1178 | 0x49a | TP_CLU_Ipod_HU | 8 | 8 |
| 410 | 0x19a | HU_CLU_PE_08 | 8 | 4 |
| 1176 | 0x498 | TP_CLU_DVD_HU | 8 | 8 |
| 1175 | 0x497 | TP_CLU_USB_HU | 8 | 8 |
| 407 | 0x197 | HU_CLU_PE_05 | 8 | 7 |
| 1942 | 0x796 | TP_AMP_HU_DiagRes | 8 | 8 |
| 406 | 0x196 | HU_CLU_PE_04 | 8 | 6 |
| 1941 | 0x795 | TP_HU_AMP_DiagReq | 8 | 8 |
| 1173 | 0x495 | TP_CLU_CD_HU | 8 | 8 |
| 405 | 0x195 | HU_CLU_PE_03 | 8 | 5 |
| 1168 | 0x490 | TP_HU_USB_CLU | 8 | 8 |
| 1936 | 0x790 | TP_HU_All_Req | 8 | 8 |
| 1167 | 0x48f | TP_HU_Ipod_CLU | 8 | 8 |
| 1166 | 0x48e | TP_HU_DVD_CLU | 8 | 8 |
| 1165 | 0x48d | TP_HU_CD_CLU | 8 | 8 |
| 1164 | 0x48c | TP_CLU_NAVI_HU | 8 | 8 |
| 139 | 0x8b | AMP_HU_E_12 | 8 | 6 |
| 138 | 0x8a | AMP_HU_E_11 | 8 | 6 |
| 137 | 0x89 | AMP_HU_E_10 | 8 | 6 |
| 1928 | 0x788 | TP_HU_PhyRes | 8 | 8 |
| 136 | 0x88 | AMP_HU_E_09 | 8 | 6 |
| 135 | 0x87 | AMP_HU_E_08 | 8 | 6 |
| 134 | 0x86 | AMP_HU_E_07 | 8 | 2 |
| 1157 | 0x485 | TP_HU_CLU_HF | 8 | 8 |
| 133 | 0x85 | AMP_HU_E_06 | 8 | 8 |
| 389 | 0x185 | AMP_HU_PE_05 | 8 | 8 |
| 132 | 0x84 | AMP_HU_E_05 | 8 | 6 |
| 388 | 0x184 | AMP_HU_PE_04 | 8 | 4 |
| 1156 | 0x484 | TP_CLU_HF_HU | 8 | 8 |
| 131 | 0x83 | AMP_HU_E_04 | 8 | 6 |
| 387 | 0x183 | AMP_HU_PE_03 | 8 | 7 |
| 130 | 0x82 | AMP_HU_E_03 | 8 | 6 |
| 129 | 0x81 | AMP_HU_E_02 | 8 | 2 |
| 385 | 0x181 | AMP_HU_PE_02 | 8 | 11 |
| 128 | 0x80 | AMP_HU_E_01 | 8 | 8 |
| 384 | 0x180 | AMP_HU_PE_01 | 8 | 14 |
| 1408 | 0x580 | AMP_HU_P_01 | 8 | 24 |
| 1920 | 0x780 | TP_HU_PhyReq | 8 | 8 |
| 371 | 0x173 | HU_TMU_PE_01 | 8 | 8 |
| 369 | 0x171 | HU_Car_PE_01 | 8 | 1 |
| 1392 | 0x570 | HU_TMU_P_01 | 8 | 1 |
| 112 | 0x70 | HU_AMP_E_09 | 8 | 6 |
| 1390 | 0x56e | GW_CLU_P | 8 | 2 |
| 363 | 0x16b | GW_IPM_PE_2 | 8 | 7 |
| 362 | 0x16a | GW_IPM_PE_1 | 8 | 24 |
| 361 | 0x169 | GW_CHASSIS_PE_1 | 8 | 3 |
| 359 | 0x167 | GW_WARNING_PE_01 | 8 | 23 |
| 1376 | 0x560 | HU_TMU_P_02 | 8 | 3 |
| 93 | 0x5d | DATC_HU_E_SYS | 8 | 4 |
| 344 | 0x158 | GW_CLU_PE | 8 | 9 |
| 87 | 0x57 | HU_E_02 | 8 | 1 |
| 343 | 0x157 | GW_WARNING_PE_02 | 8 | 4 |
| 75 | 0x4b | HU_AMP_E_12 | 8 | 8 |
| 74 | 0x4a | HU_AMP_E_11 | 8 | 4 |
| 1864 | 0x748 | TP_AMP_EDT | 8 | 8 |
| 327 | 0x147 | TMU_HU_PE_03 | 8 | 10 |
| 326 | 0x146 | TMU_HU_PE_02 | 8 | 7 |
| 325 | 0x145 | TMU_HU_PE_01 | 8 | 10 |
| 69 | 0x45 | TMU_HU_E_04 | 8 | 1 |
| 67 | 0x43 | TMU_GW_E_01 | 8 | 5 |
| 66 | 0x42 | TMU_HU_E_03 | 8 | 2 |
| 1345 | 0x541 | TMU_HU_P_02 | 8 | 7 |
| 65 | 0x41 | TMU_HU_E_02 | 8 | 10 |
| 1344 | 0x540 | TMU_HU_P_01 | 8 | 5 |
| 64 | 0x40 | TMU_HU_E_01 | 8 | 8 |
| 62 | 0x3e | HU_Navi_E_00 | 8 | 6 |
| 52 | 0x34 | HU_DATC_E_02 | 8 | 24 |
| 308 | 0x134 | DATC_PE_05 | 8 | 21 |
| 307 | 0x133 | DATC_PE_04 | 8 | 16 |
| 306 | 0x132 | DATC_PE_03 | 8 | 22 |
| 1329 | 0x531 | DATC_P_02 | 8 | 2 |
| 305 | 0x131 | DATC_PE_02 | 8 | 8 |
| 304 | 0x130 | DATC_PE_01 | 8 | 7 |
| 291 | 0x123 | HU_CLU_PE_07 | 8 | 14 |
| 290 | 0x122 | HU_CLU_PE_06 | 8 | 15 |
| 286 | 0x11e | HU_CLU_PE_10 | 8 | 1 |
| 29 | 0x1d | CLU_HU_E_00 | 8 | 3 |
| 27 | 0x1b | AMP_HU_E_00 | 8 | 1 |
| 23 | 0x17 | HU_IPM_E_00 | 8 | 20 |
| 277 | 0x115 | HU_CLU_PE_02 | 8 | 8 |
| 276 | 0x114 | HU_CLU_PE_01 | 8 | 10 |
| 17 | 0x11 | HU_AMP_E_10 | 8 | 6 |
| 15 | 0xf | HU_AMP_E_08 | 8 | 6 |
| 14 | 0xe | HU_AMP_E_07 | 8 | 4 |
| 13 | 0xd | HU_AMP_E_06 | 8 | 4 |
| 12 | 0xc | HU_AMP_E_05 | 8 | 4 |
| 11 | 0xb | HU_AMP_E_04 | 8 | 2 |
| 10 | 0xa | HU_AMP_E_03 | 8 | 5 |
| 9 | 0x9 | HU_AMP_E_02 | 8 | 13 |
| 1288 | 0x508 | HU_CLU_P_02 | 8 | 3 |
| 8 | 0x8 | HU_AMP_E_01 | 8 | 10 |
| 1287 | 0x507 | HU_CLU_P_01 | 8 | 7 |
| 1286 | 0x506 | HU_CLU_P_00 | 8 | 8 |
| 1284 | 0x504 | HU_AMP_P_01 | 8 | 4 |
| 256 | 0x100 | HU_MON_PE_01 | 8 | 8 |
| 1092 | 0x444 | NM_CLOCK | 8 | 3 |
| 1108 | 0x454 | NM_HUD | 8 | 3 |
| 1088 | 0x440 | NM_H_U | 8 | 3 |
| 1091 | 0x443 | NM_DATC | 8 | 3 |
| 1105 | 0x451 | NM_CCP | 8 | 3 |
| 1100 | 0x44c | NM_KMA_TMU | 8 | 3 |
| 1098 | 0x44a | NM_CUBIS | 8 | 3 |
| 1099 | 0x44b | NM_TMU | 8 | 3 |
| 1095 | 0x447 | NM_IPM | 8 | 3 |
| 1107 | 0x453 | NM_RSE_R | 8 | 3 |
| 1093 | 0x445 | NM_RRC | 8 | 3 |
| 1109 | 0x455 | NM_CGW | 8 | 3 |
| 1106 | 0x452 | NM_RSE_L | 8 | 3 |
| 1096 | 0x448 | NM_AMP | 8 | 3 |
| 1103 | 0x44f | NM_EDT | 8 | 3 |
| 1110 | 0x456 | NM_SWRC | 8 | 3 |
| 1102 | 0x44e | NM_IBOX | 8 | 3 |
| 1101 | 0x44d | NM_CLU | 8 | 3 |
| 1097 | 0x449 | NM_FHCU | 8 | 3 |
| 1094 | 0x446 | NM_ASD | 8 | 3 |
| 1089 | 0x441 | NM_MON | 8 | 3 |
| 1104 | 0x450 | NM_AVM | 8 | 3 |
| 1090 | 0x442 | NM_KBD | 8 | 3 |

## hyundai_i30_2014 — Hyundai i30 2014 [B]

- Make: hyundai; Full-vehicle CAN
- Messages: 32; signals: 415
- Evidence: opendbc/opendbc/dbc/hyundai_i30_2014.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 128 | 0x80 | EMS_DCT1 | 8 | 10 |
| 129 | 0x81 | EMS_DCT2 | 8 | 6 |
| 160 | 0xa0 | EngFrzFrm1 | 8 | 6 |
| 161 | 0xa1 | EngFrzFrm2 | 8 | 6 |
| 304 | 0x130 | YRS1 | 8 | 7 |
| 305 | 0x131 | YRS3 | 8 | 6 |
| 320 | 0x140 | YRS2 | 8 | 7 |
| 339 | 0x153 | TCS1 | 8 | 30 |
| 356 | 0x164 | VSM1 | 8 | 6 |
| 357 | 0x165 | VSM2 | 8 | 6 |
| 399 | 0x18f | EMS_H2 | 8 | 21 |
| 497 | 0x1f1 | TCS5 | 8 | 12 |
| 544 | 0x220 | ESP2 | 8 | 17 |
| 608 | 0x260 | EMS6 | 8 | 15 |
| 672 | 0x2a0 | EMS5 | 8 | 13 |
| 688 | 0x2b0 | SAS1 | 8 | 5 |
| 790 | 0x316 | EMS1 | 8 | 13 |
| 809 | 0x329 | EMS2 | 8 | 19 |
| 848 | 0x350 | FATC | 8 | 19 |
| 880 | 0x370 | TCU3 | 8 | 19 |
| 898 | 0x382 | EMS9 | 8 | 13 |
| 1075 | 0x433 | EPB1 | 8 | 14 |
| 1087 | 0x43f | TCU1 | 8 | 14 |
| 1088 | 0x440 | TCU2 | 8 | 14 |
| 1200 | 0x4b0 | WHL_SPD | 8 | 4 |
| 1201 | 0x4b1 | WHL_PUL | 8 | 9 |
| 1264 | 0x4f0 | CLU1 | 8 | 15 |
| 1265 | 0x4f1 | CLU3 | 8 | 28 |
| 1349 | 0x545 | EMS4 | 8 | 9 |
| 1435 | 0x59b | TCU4 | 8 | 14 |
| 1508 | 0x5e4 | MDPS1 | 8 | 5 |
| 1680 | 0x690 | CLU2 | 8 | 33 |

## hyundai_santafe_2007 — Hyundai Santa Fe 2007 [B]

- Make: hyundai; Full-vehicle CAN
- Messages: 13; signals: 49
- Evidence: opendbc/opendbc/dbc/hyundai_santafe_2007.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 339 | 0x153 | ESP_Flags | 8 | 8 |
| 497 | 0x1f1 | ESP_WheelSpeed | 8 | 4 |
| 608 | 0x260 | ECU_Data1 | 8 | 6 |
| 640 | 0x280 | ECU_Data2 | 8 | 4 |
| 688 | 0x2b0 | SAS_Data | 5 | 5 |
| 809 | 0x329 | ECU_Data5 | 8 | 3 |
| 1064 | 0x428 | AWD_Data1 | 8 | 2 |
| 1065 | 0x429 | AWD_Data2 | 8 | 5 |
| 1087 | 0x43f | TCU_Data | 8 | 4 |
| 1349 | 0x545 | ECU_Data6 | 8 | 1 |
| 1408 | 0x580 | ABS_WheelSpeed | 8 | 4 |
| 1695 | 0x69f | ECU_Data7 | 8 | 1 |
| 1984 | 0x7c0 | SAS_Calibration | 2 | 2 |

## nissan_xterra_2011 — Nissan Xterra 2011 [B]

- Make: nissan; Full-vehicle CAN (fragment)
- Messages: 15; signals: 30
- Evidence: opendbc/opendbc/dbc/nissan_xterra_2011.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 2 | 0x2 | STEERING | 5 | 3 |
| 505 | 0x1f9 | ENGINE_1 | 8 | 3 |
| 561 | 0x231 | ENGINE_2 | 8 | 1 |
| 563 | 0x233 | ENGINE_7 | 8 | 3 |
| 573 | 0x23d | ENGINE_3 | 8 | 4 |
| 574 | 0x23e | ENGINE_4 | 8 | 3 |
| 595 | 0x253 | TCU_1 | 8 | 2 |
| 640 | 0x280 | SPEED | 8 | 1 |
| 644 | 0x284 | ABS_1 | 8 | 2 |
| 645 | 0x285 | ABS_2 | 8 | 2 |
| 852 | 0x354 | SPEED_BREAK | 8 | 3 |
| 861 | 0x35d | BCM | 8 | 0 |
| 1361 | 0x551 | ENGINE_5 | 8 | 1 |
| 1408 | 0x580 | ENGINE_6 | 8 | 2 |
| 1477 | 0x5c5 | MILEAGE | 8 | 0 |

## subaru_forester_2017 — Subaru Global Platform [B]

- Make: subaru; Forester 2017; Subaru Global Platform underpins 2017+ models
- Messages: 2; signals: 13
- Evidence: opendbc/opendbc/dbc/generator/subaru/subaru_forester_2017.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 355 | 0x163 | ES_DashStatus | 8 | 8 |
| 881 | 0x371 | Steering_Torque | 8 | 5 |

## subaru_global_2017 — Subaru Global Platform [B]

- Make: subaru; Global-platform reference capture, 2017
- Messages: 5; signals: 42
- Evidence: opendbc/opendbc/dbc/generator/subaru/subaru_global_2017.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 72 | 0x48 | Transmission | 8 | 4 |
| 73 | 0x49 | CVT | 8 | 3 |
| 545 | 0x221 | ES_Distance | 8 | 20 |
| 546 | 0x222 | ES_Status | 8 | 9 |
| 576 | 0x240 | CruiseControl | 8 | 6 |

## subaru_global_2020_hybrid — Subaru Global Platform [B]

- Make: subaru; Global-platform hybrid reference capture, 2020
- Messages: 4; signals: 7
- Evidence: opendbc/opendbc/dbc/generator/subaru/subaru_global_2020_hybrid.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 39 | 0x27 | Cruise_Status_2 | 8 | 1 |
| 295 | 0x127 | Transmission | 8 | 1 |
| 360 | 0x168 | Throttle_Hybrid | 8 | 3 |
| 550 | 0x226 | Brake_Hybrid | 8 | 2 |

## subaru_outback_2015 — Subaru SJ platform [B]

- Make: subaru; Outback 2015 (pre-global SJ platform)
- Messages: 2; signals: 21
- Evidence: opendbc/opendbc/dbc/generator/subaru/subaru_outback_2015.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 358 | 0x166 | ES_DashStatus | 8 | 16 |
| 881 | 0x371 | Steering_Torque | 8 | 5 |

## subaru_outback_2019 — Subaru Global Platform [B]

- Make: subaru; Outback 2019 (global platform)
- Messages: 2; signals: 21
- Evidence: opendbc/opendbc/dbc/generator/subaru/subaru_outback_2019.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 358 | 0x166 | ES_DashStatus | 8 | 16 |
| 881 | 0x371 | Steering_Torque | 8 | 5 |

## mazda_2017 — Mazda SkyActiv [B]

- Make: mazda; Mazda reference capture, 2017 (SkyActiv era)
- Messages: 102; signals: 515
- Evidence: opendbc/opendbc/dbc/mazda_2017.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 117 | 0x75 | STEER_RELATED | 8 | 8 |
| 118 | 0x76 | RPM_RELATED | 8 | 2 |
| 514 | 0x202 | ENGINE_DATA | 8 | 4 |
| 357 | 0x165 | PEDALS | 8 | 12 |
| 533 | 0x215 | WHEEL_SPEEDS | 8 | 4 |
| 134 | 0x86 | STEER2 | 8 | 9 |
| 576 | 0x240 | STEER_TORQUE | 8 | 7 |
| 577 | 0x241 | STEER_RATE | 8 | 8 |
| 582 | 0x246 | CAM_LANEMAYBE | 8 | 5 |
| 541 | 0x21d | CAM_EMPTY | 8 | 0 |
| 605 | 0x25d | CAM_PEDESTRIAN | 8 | 7 |
| 578 | 0x242 | CAM_LANETRACK | 8 | 9 |
| 579 | 0x243 | CAM_LKAS | 8 | 10 |
| 580 | 0x244 | CAM_DISTANCE | 8 | 7 |
| 581 | 0x245 | CAM_IDK3 | 8 | 9 |
| 863 | 0x35f | CAM_TRAFFIC_SIGNS | 8 | 8 |
| 1157 | 0x485 | CAM_SETTINGS | 8 | 11 |
| 1160 | 0x488 | CAM_Empty3 | 8 | 1 |
| 1088 | 0x440 | CAM_LANEINFO | 8 | 17 |
| 1479 | 0x5c7 | NEW_MSG_470 | 8 | 0 |
| 1456 | 0x5b0 | NEW_MSG_300 | 8 | 0 |
| 1446 | 0x5a6 | NEW_MSG_a600 | 8 | 0 |
| 1416 | 0x588 | MSG_18 | 8 | 0 |
| 1086 | 0x43e | DOORS | 8 | 12 |
| 977 | 0x3d1 | TWO_STATES | 8 | 8 |
| 1085 | 0x43d | MSG_12 | 8 | 6 |
| 159 | 0x9f | MSG_11 | 8 | 2 |
| 1278 | 0x4fe | NEW_MSG_3 | 8 | 7 |
| 1277 | 0x4fd | NEW_MSG_10 | 8 | 3 |
| 1275 | 0x4fb | 20175 | 8 | 1 |
| 1274 | 0x4fa | NEW_MSG_12 | 8 | 5 |
| 1180 | 0x49c | last_byte_roughRPM | 8 | 1 |
| 1078 | 0x436 | HVAC | 8 | 4 |
| 1056 | 0x420 | CHECK_AND_TEMP | 8 | 9 |
| 1045 | 0x415 | TRACTION | 8 | 13 |
| 1034 | 0x40a | MSG_07 | 8 | 9 |
| 870 | 0x366 | RADAR_366_STATIC | 8 | 7 |
| 867 | 0x363 | RADAR_363 | 8 | 9 |
| 130 | 0x82 | STEER | 8 | 5 |
| 120 | 0x78 | BRAKE | 8 | 4 |
| 304 | 0x130 | GEAR_RELATED | 8 | 2 |
| 865 | 0x361 | RADAR_DISTANCE | 8 | 6 |
| 836 | 0x344 | NEW_MSG_19 | 8 | 2 |
| 832 | 0x340 | SEATBELT | 8 | 6 |
| 866 | 0x362 | RADAR_TURN | 8 | 9 |
| 158 | 0x9e | MSG_05 | 8 | 3 |
| 157 | 0x9d | CRZ_BTNS | 8 | 20 |
| 154 | 0x9a | BLINK_INFO | 8 | 10 |
| 145 | 0x91 | TURN_SWITCH | 8 | 5 |
| 80 | 0x50 | MSG_04 | 8 | 2 |
| 978 | 0x3d2 | MSG_03 | 8 | 8 |
| 607 | 0x25f | NEW_MSG_25 | 8 | 0 |
| 1115 | 0x45b | MSG_02 | 8 | 7 |
| 1067 | 0x42b | NEW_MSG_27 | 8 | 9 |
| 358 | 0x166 | NEW_MSG_28 | 8 | 0 |
| 608 | 0x260 | NEW_MSG_29 | 8 | 1 |
| 606 | 0x25e | SPEED_TBD | 8 | 2 |
| 552 | 0x228 | GEAR | 8 | 7 |
| 543 | 0x21f | CRZ_EVENTS | 8 | 11 |
| 542 | 0x21e | NEW_MSG_33 | 8 | 2 |
| 868 | 0x364 | RADAR_364 | 8 | 9 |
| 869 | 0x365 | RADAR_365 | 8 | 7 |
| 1114 | 0x45a | NEW_MSG_4 | 8 | 0 |
| 535 | 0x217 | CURVE_CTRS | 8 | 19 |
| 540 | 0x21c | CRZ_CTRL | 8 | 19 |
| 539 | 0x21b | CRZ_INFO | 8 | 10 |
| 121 | 0x79 | EPB | 8 | 12 |
| 1070 | 0x42e | 20171 | 8 | 0 |
| 1183 | 0x49f | 20172 | 8 | 0 |
| 1243 | 0x4db | 20173 | 8 | 1 |
| 1269 | 0x4f5 | MSG_2017_4 | 8 | 1 |
| 1178 | 0x49a | 20176 | 8 | 1 |
| 1179 | 0x49b | 20177 | 8 | 1 |
| 1435 | 0x59b | 20178 | 8 | 0 |
| 253 | 0xfd | GAS | 8 | 5 |
| 359 | 0x167 | MORE_GAS | 8 | 7 |
| 512 | 0x200 | NEW_MSG_30 | 8 | 12 |
| 515 | 0x203 | MSG_01 | 8 | 4 |
| 529 | 0x211 | NEW_MSG_36 | 8 | 7 |
| 1242 | 0x4da | NEW_MSG_37 | 8 | 0 |
| 1266 | 0x4f2 | MSG_09 | 8 | 3 |
| 976 | 0x3d0 | MSG_15 | 8 | 2 |
| 155 | 0x9b | MSG_14 | 8 | 0 |
| 1267 | 0x4f3 | MSG_10 | 8 | 2 |
| 305 | 0x131 | NEW_MSG_6 | 8 | 3 |
| 1238 | 0x4d6 | TEMPERATURE | 8 | 1 |
| 1087 | 0x43f | NEW_MSG_1 | 8 | 1 |
| 1143 | 0x477 | BSM | 8 | 13 |
| 480 | 0x1e0 | ACCEL_TEST | 8 | 4 |
| 1361 | 0x551 | KEY_POSITION | 8 | 0 |
| 1283 | 0x503 | KEY_POSITION2 | 8 | 0 |
| 628 | 0x274 | MSG_06 | 8 | 0 |
| 1154 | 0x482 | MSG_08 | 8 | 0 |
| 1139 | 0x473 | MSG_13 | 8 | 0 |
| 1270 | 0x4f6 | MSG_16 | 8 | 0 |
| 1272 | 0x4f8 | MSG_17 | 8 | 0 |
| 1425 | 0x591 | MSG_19 | 8 | 0 |
| 70 | 0x46 | MOB1 | 8 | 5 |
| 64 | 0x40 | MOB2 | 8 | 11 |
| 1171 | 0x493 | MOB3 | 8 | 0 |
| 1248 | 0x4e0 | MOB4 | 8 | 0 |
| 1177 | 0x499 | RADAR_499_STATIC | 8 | 0 |

## mazda_3_2019 — Mazda SkyActiv-Vehicle Architecture [B]

- Make: mazda; Mazda3 2019 (SkyActiv-Vehicle Architecture)
- Messages: 59; signals: 246
- Evidence: opendbc/opendbc/dbc/mazda_3_2019.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 256 | 0x100 | CAM_Start | 8 | 9 |
| 358 | 0x166 | CAM_End | 8 | 3 |
| 1216 | 0x4c0 | CAM_69 | 8 | 5 |
| 1120 | 0x460 | CAM_KEEP_ALIVE_2 | 8 | 4 |
| 1436 | 0x59c | CAM_71 | 8 | 4 |
| 18 | 0x12 | STEER | 8 | 6 |
| 257 | 0x101 | LKAS | 8 | 9 |
| 258 | 0x102 | NEW_MSG_3 | 8 | 6 |
| 28 | 0x1c | WHEEL_SPEEDS | 8 | 4 |
| 259 | 0x103 | NEW_MSG_5 | 8 | 4 |
| 260 | 0x104 | NEW_MSG_6 | 8 | 3 |
| 261 | 0x105 | NEW_MSG_7 | 8 | 1 |
| 262 | 0x106 | NEW_MSG_8 | 8 | 2 |
| 263 | 0x107 | NEW_MSG_9 | 8 | 1 |
| 310 | 0x136 | NEW_MSG_10 | 8 | 3 |
| 308 | 0x134 | ACC_POSSIBLY | 8 | 8 |
| 304 | 0x130 | CAM_LANES | 8 | 8 |
| 305 | 0x131 | CAM_LANES_2_MAYBE | 8 | 8 |
| 352 | 0x160 | NEW_MSG_14 | 8 | 4 |
| 355 | 0x163 | NEW_MSG_15 | 8 | 1 |
| 356 | 0x164 | NEW_MSG_16 | 8 | 2 |
| 357 | 0x165 | NEW_MSG_17 | 8 | 3 |
| 59 | 0x3b | STEER_RATE | 8 | 5 |
| 24 | 0x18 | BRAKE_PEDAL | 8 | 4 |
| 26 | 0x1a | ENGINE_DATA | 8 | 4 |
| 145 | 0x91 | BLINK_INFO | 8 | 5 |
| 16 | 0x10 | STEER_TORQUE | 8 | 9 |
| 17 | 0x11 | STEER_TORQUE_2 | 8 | 7 |
| 29 | 0x1d | WHEEL | 8 | 7 |
| 31 | 0x1f | GEAR | 8 | 4 |
| 96 | 0x60 | STEER2 | 8 | 12 |
| 1209 | 0x4b9 | KEEP_ALIVE_1 | 8 | 8 |
| 37 | 0x25 | BLANK_1 | 8 | 4 |
| 44 | 0x2c | BLANK_2 | 8 | 4 |
| 128 | 0x80 | RADARS | 8 | 8 |
| 129 | 0x81 | NEW_MSG_19 | 8 | 4 |
| 1034 | 0x40a | KEEP_ALIVE_2 | 8 | 4 |
| 1200 | 0x4b0 | KEEP_ALIVE_3 | 8 | 4 |
| 354 | 0x162 | CAM_KEEP_ALIVE_1 | 8 | 4 |
| 336 | 0x150 | NEW_MSG_20 | 8 | 5 |
| 342 | 0x156 | NEW_MSG_21 | 8 | 8 |
| 264 | 0x108 | NEW_MSG_2 | 8 | 3 |
| 22 | 0x16 | CRZ_CTRL_BTNS | 8 | 4 |
| 306 | 0x132 | CAM_LANE_3_MAYBE | 8 | 6 |
| 307 | 0x133 | NEW_MSG_1 | 8 | 5 |
| 320 | 0x140 | NEW_MSG_4 | 8 | 4 |
| 321 | 0x141 | NEW_MSG_11 | 8 | 2 |
| 293 | 0x125 | NEW_MSG_12 | 8 | 3 |
| 294 | 0x126 | NEW_MSG_13 | 8 | 3 |
| 292 | 0x124 | NEW_MSG_18 | 8 | 1 |
| 291 | 0x123 | NEW_MSG_22 | 8 | 1 |
| 290 | 0x122 | NEW_MSG_23 | 8 | 1 |
| 277 | 0x115 | NEW_MSG_24 | 8 | 1 |
| 278 | 0x116 | NEW_MSG_25 | 8 | 0 |
| 273 | 0x111 | NEW_MSG_26 | 8 | 1 |
| 274 | 0x112 | NEW_MSG_27 | 8 | 1 |
| 289 | 0x121 | NEW_MSG_28 | 8 | 1 |
| 20 | 0x14 | NEW_MSG_29 | 8 | 1 |
| 288 | 0x120 | NEW_MSG_30 | 8 | 0 |

## mazda_radar — Mazda SkyActiv [B]

- Make: mazda; Mazda radar/ADAS bus capture
- Messages: 9; signals: 18
- Evidence: opendbc/opendbc/dbc/mazda_radar.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 540 | 0x21c | CRZ_CTRL | 8 | 0 |
| 539 | 0x21b | CRZ_INFO | 8 | 0 |
| 865 | 0x361 | RADAR_TRACK_361 | 8 | 3 |
| 866 | 0x362 | RADAR_TRACK_362 | 8 | 3 |
| 867 | 0x363 | RADAR_TRACK_363 | 8 | 3 |
| 868 | 0x364 | RADAR_TRACK_364 | 8 | 3 |
| 869 | 0x365 | RADAR_TRACK_365 | 8 | 3 |
| 870 | 0x366 | RADAR_TRACK_366 | 8 | 3 |
| 1177 | 0x499 | RADAR_499 | 8 | 0 |

## mazda_rx8 — Mazda RX-8 [B]

- Make: mazda; RX-8 (pre-SkyActiv, rotary)
- Messages: 7; signals: 17
- Evidence: opendbc/opendbc/dbc/mazda_rx8.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 129 | 0x81 | steering | 8 | 1 |
| 513 | 0x201 | speed | 8 | 3 |
| 592 | 0x250 | throttle_body | 8 | 3 |
| 658 | 0x292 | brake_controls | 8 | 2 |
| 1056 | 0x420 | coolant | 8 | 1 |
| 1072 | 0x430 | instrument_cluster | 8 | 3 |
| 1200 | 0x4b0 | wheel_speed | 8 | 4 |

## bmw_e9x_e8x — BMW E9x/E8x [B]

- Make: bmw; 3-series E9x / 1-series E8x (pre-Fxx, PT-CAN/K-CAN era)
- Messages: 326; signals: 165
- Evidence: opendbc/opendbc/dbc/bmw_e9x_e8x.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 170 | 0xaa | AccPedal | 8 | 9 |
| 404 | 0x194 | CruiseControl | 4 | 11 |
| 512 | 0x200 | CruiseControlStatus | 8 | 3 |
| 168 | 0xa8 | EngineAndBrake | 8 | 11 |
| 470 | 0x1d6 | SteeringButtons | 2 | 6 |
| 403 | 0x193 | DynamicCruiseControlStatus | 8 | 4 |
| 201 | 0xc9 | SteeringWheelAngle_DSC | 8 | 3 |
| 206 | 0xce | WheelSpeeds | 8 | 4 |
| 884 | 0x374 | WheelToleranceAdjustment | 8 | 0 |
| 678 | 0x2a6 | WiperSwitch | 8 | 1 |
| 304 | 0x130 | TerminalStatus | 8 | 4 |
| 169 | 0xa9 | Torque2 | 8 | 8 |
| 184 | 0xb8 | TorqueTransmisionRequest | 8 | 2 |
| 196 | 0xc4 | SteeringWheelAngle | 7 | 2 |
| 180 | 0xb4 | WheelTorqueDriveTrain1 | 8 | 0 |
| 182 | 0xb6 | DynamicCruiseControlTorqueDemand | 8 | 3 |
| 186 | 0xba | TransmissionData | 8 | 6 |
| 191 | 0xbf | RequestedWheelTorqueDriveTrain | 8 | 3 |
| 414 | 0x19e | StatusDSC_KCAN | 8 | 6 |
| 416 | 0x1a0 | Speed | 8 | 8 |
| 418 | 0x1a2 | TransimissionData2 | 8 | 3 |
| 690 | 0x2b2 | WheelPressure_KCAN | 8 | 0 |
| 691 | 0x2b3 | AccelerationData | 8 | 0 |
| 402 | 0x192 | GearSelectorSwitch_1 | 4 | 1 |
| 408 | 0x198 | GearSelectorSwitch | 8 | 15 |
| 422 | 0x1a6 | DistanceRoute | 8 | 0 |
| 436 | 0x1b4 | InstrumentClusterStatus_KOMBI | 8 | 1 |
| 464 | 0x1d0 | EngineData | 8 | 9 |
| 945 | 0x3b1 | TransmissionData3 | 8 | 2 |
| 200 | 0xc8 | SteeringWheelAngle_slow | 6 | 3 |
| 466 | 0x1d2 | TransmissionDataDisplay | 8 | 7 |
| 437 | 0x1b5 | HeatFlow_LoadTorqueClimate | 8 | 0 |
| 1152 | 0x480 | NetworkManagment1 | 8 | 0 |
| 1170 | 0x492 | NetworkManagment2 | 8 | 0 |
| 1175 | 0x497 | NetworkManagment3 | 8 | 0 |
| 1176 | 0x498 | NetworkManagment4 | 8 | 0 |
| 1193 | 0x4a9 | NetworkManagment5 | 8 | 0 |
| 1246 | 0x4de | GWS_ShiftLeverHeartbeat | 8 | 1 |
| 438 | 0x1b6 | HeatFlowEngine | 8 | 0 |
| 784 | 0x310 | AmbientTemperature_RelativeTime | 8 | 0 |
| 821 | 0x335 | ElectricFuelPumpStatus | 8 | 0 |
| 1007 | 0x3ef | EngineOBD_data | 8 | 0 |
| 1432 | 0x598 | ServicesDKG | 8 | 0 |
| 309 | 0x135 | CrashDisconnectControl | 8 | 0 |
| 502 | 0x1f6 | TurnSignals | 2 | 5 |
| 514 | 0x202 | Dimming | 8 | 0 |
| 538 | 0x21a | LampStatus | 8 | 0 |
| 550 | 0x226 | RainSensorWiperSpeed | 8 | 0 |
| 578 | 0x242 | ClimateFrontStatus | 8 | 0 |
| 704 | 0x2c0 | LCD_lighting | 8 | 0 |
| 758 | 0x2f6 | LightControl | 8 | 0 |
| 760 | 0x2f8 | Time_Date | 8 | 0 |
| 762 | 0x2fa | OccupancySeatBeltContact | 8 | 2 |
| 764 | 0x2fc | TrunkStatus | 8 | 0 |
| 797 | 0x31d | TirePressureStatus | 8 | 0 |
| 816 | 0x330 | Range_Mileage | 8 | 0 |
| 823 | 0x337 | StatusFuelControl | 8 | 0 |
| 897 | 0x381 | EngineOilLevel | 8 | 0 |
| 940 | 0x3ac | RunOnTimeTerminal30 | 8 | 0 |
| 947 | 0x3b3 | PowerManagmentConsumptionControl | 8 | 0 |
| 948 | 0x3b4 | PowerBatteryVoltage | 8 | 1 |
| 958 | 0x3be | PowerRunningTime | 8 | 0 |
| 1408 | 0x580 | ServicesKGM | 8 | 0 |
| 1426 | 0x592 | ServicesDME | 8 | 0 |
| 1449 | 0x5a9 | ServicesDSC | 8 | 0 |
| 1504 | 0x5e0 | ServicesKOMBI | 8 | 0 |
| 1522 | 0x5f2 | ServicesKBM | 8 | 0 |
| 209 | 0xd1 | Accelerometer1 | 8 | 5 |
| 172 | 0xac | WheelTorqueDrivetrain2 | 8 | 0 |
| 128 | 0x80 | SYNC | 5 | 3 |
| 320 | 0x140 | Unknown140 | 2 | 1 |
| 212 | 0xd4 | Unknown_d4 | 8 | 3 |
| 205 | 0xcd | Accelerometer2 | 8 | 4 |
| 790 | 0x316 | OperationPushButtonDTC | 2 | 2 |
| 1577 | 0x629 | Unknown_629 | 8 | 0 |
| 133 | 0x85 | Synchronization_SC_VDA | 8 | 0 |
| 173 | 0xad | Delay_request_ACC | 8 | 0 |
| 177 | 0xb1 | Torque_request_steering | 8 | 0 |
| 181 | 0xb5 | Torque_request_EGS | 8 | 2 |
| 183 | 0xb7 | Torque_request_ACC | 8 | 0 |
| 187 | 0xbb | Target_torque_request | 8 | 0 |
| 188 | 0xbc | Status_target_torque_conversion | 8 | 0 |
| 190 | 0xbe | Alive_Counter | 8 | 0 |
| 192 | 0xc0 | Alive_Central_Gateway | 8 | 0 |
| 193 | 0xc1 | Alive_counter_telephone | 8 | 0 |
| 213 | 0xd5 | Request_wheel_torque_brake | 8 | 0 |
| 215 | 0xd7 | Alive_Counter_Security | 8 | 0 |
| 216 | 0xd8 | CLU1_VDA | 8 | 0 |
| 225 | 0xe1 | Wheel_torque_brake | 8 | 0 |
| 226 | 0xe2 | Status_central_locking_BFT | 8 | 0 |
| 227 | 0xe3 | CLU2_VDA | 8 | 0 |
| 230 | 0xe6 | Status_central_locking_BFTH | 8 | 0 |
| 234 | 0xea | Status_central_locking_FAT | 8 | 0 |
| 238 | 0xee | Central_locking_status_FATH | 8 | 0 |
| 242 | 0xf2 | Status_central_locking_HK | 8 | 0 |
| 244 | 0xf4 | CLU3_VDA | 8 | 0 |
| 247 | 0xf7 | lateral_dynamics_ARS_VDM | 8 | 0 |
| 249 | 0xf9 | Vertical_dynamics_VDM_ARS | 8 | 0 |
| 250 | 0xfa | Control_window_lifter_FAT | 8 | 0 |
| 251 | 0xfb | Control_window_lifter_BFT | 8 | 0 |
| 252 | 0xfc | Control_window_lifter_FATH | 8 | 0 |
| 253 | 0xfd | Control_window_lifter_BFTH | 8 | 0 |
| 254 | 0xfe | Voltage_level_sensors | 8 | 0 |
| 280 | 0x118 | Exchange_AFS_DSC | 8 | 0 |
| 286 | 0x11e | Control_interventions_DSC_AFS | 8 | 0 |
| 288 | 0x120 | Status_partial_setpoints_AFS_DSC_2 | 8 | 0 |
| 298 | 0x12a | Sensor_data_ROSE | 8 | 0 |
| 300 | 0x12c | input_data_ROSE | 8 | 0 |
| 336 | 0x150 | Request_1_ACC | 8 | 0 |
| 339 | 0x153 | Request_2_ACC | 8 | 0 |
| 345 | 0x159 | Object_data_ACC | 8 | 0 |
| 348 | 0x15c | Status_ACC | 8 | 0 |
| 351 | 0x15f | Requirement_angle_FFP | 8 | 0 |
| 357 | 0x165 | CLU_Status_VDA | 8 | 0 |
| 370 | 0x172 | Acknowledgment_request_Kombination | 8 | 0 |
| 373 | 0x175 | Display_motor_data | 8 | 0 |
| 400 | 0x190 | display_ACC | 8 | 0 |
| 405 | 0x195 | Operation_push_button_MSA | 8 | 0 |
| 419 | 0x1a3 | Raw_data_longitudinal_acceleration | 8 | 0 |
| 423 | 0x1a7 | actuation_request_EMF | 8 | 0 |
| 426 | 0x1aa | Effect_ErgoCommander | 8 | 0 |
| 428 | 0x1ac | Status_ARS_module | 8 | 0 |
| 440 | 0x1b8 | Operation_ErgoCommander | 8 | 0 |
| 450 | 0x1c2 | Distance_message_PDC | 8 | 0 |
| 451 | 0x1c3 | Distance_message_2_PDC | 8 | 0 |
| 454 | 0x1c6 | Acoustic_message_PDC | 8 | 0 |
| 472 | 0x1d8 | Operation_air_conditioning_air_distribution_FA | 8 | 0 |
| 473 | 0x1d9 | Operation_pushbutton_MDrive | 8 | 0 |
| 474 | 0x1da | Climate_control_remote_control | 8 | 0 |
| 476 | 0x1dc | Operation_stratification_seat_heating | 8 | 0 |
| 478 | 0x1de | Air_conditioning_controls_rear | 8 | 0 |
| 480 | 0x1e0 | Operation_air_conditioning_air_distribution_BF | 8 | 0 |
| 482 | 0x1e2 | Operation_air_conditioning_front | 8 | 0 |
| 483 | 0x1e3 | Operation_pushbutton_interior_lighting | 8 | 0 |
| 487 | 0x1e7 | Operation_seat_heating_seat_climate_FA | 8 | 0 |
| 488 | 0x1e8 | Operation_seat_heating_seat_climate_BF | 8 | 0 |
| 490 | 0x1ea | Steering_column_adjustment_control | 8 | 0 |
| 491 | 0x1eb | Operation_active_seat_FA | 8 | 0 |
| 492 | 0x1ec | Operation_active_seat_BF | 8 | 0 |
| 494 | 0x1ee | Steering_column_switch_operation | 8 | 0 |
| 499 | 0x1f3 | Operation_seat_memory_FA | 8 | 0 |
| 504 | 0x1f8 | Operation_SHD_MDS | 8 | 0 |
| 507 | 0x1fb | Status_EPS | 8 | 0 |
| 508 | 0x1fc | Status_AFS | 8 | 0 |
| 509 | 0x1fd | Status_request_EMF_KCAN | 8 | 0 |
| 510 | 0x1fe | Crash | 8 | 0 |
| 513 | 0x201 | Status_EMF_KCAN | 8 | 0 |
| 517 | 0x205 | Acoustic_request_Kombi | 8 | 0 |
| 518 | 0x206 | Control_Display_Shiftlights | 8 | 0 |
| 523 | 0x20b | Memory_adjustment | 8 | 0 |
| 524 | 0x20c | Steering_column_control | 8 | 0 |
| 525 | 0x20d | Position_steering_column | 8 | 0 |
| 528 | 0x210 | Operation_HUD | 8 | 0 |
| 529 | 0x211 | Status_HUD | 8 | 0 |
| 530 | 0x212 | Height_levels_air_spring | 8 | 0 |
| 540 | 0x21c | Operation_NightVision | 8 | 0 |
| 542 | 0x21e | Status_NightVision | 8 | 0 |
| 548 | 0x224 | Operation_push_button_NSW | 8 | 0 |
| 552 | 0x228 | Operation_special_function | 8 | 0 |
| 554 | 0x22a | Status_BFS | 8 | 0 |
| 556 | 0x22c | Operation_push_button_NSL | 8 | 0 |
| 558 | 0x22e | Status_BFSH | 8 | 0 |
| 562 | 0x232 | Status_FAS | 8 | 0 |
| 566 | 0x236 | Status_FASH | 8 | 0 |
| 570 | 0x23a | Status_radio_key | 8 | 0 |
| 571 | 0x23b | Status_climate_front_extended | 8 | 0 |
| 573 | 0x23d | Request_display_climate | 8 | 0 |
| 574 | 0x23e | Status_Klima_Fond | 8 | 0 |
| 582 | 0x246 | Status_air_conditioning_front_control_unit | 8 | 0 |
| 584 | 0x248 | Status_rear_view_camera | 8 | 0 |
| 585 | 0x249 | Control_rear_view_camera | 8 | 0 |
| 586 | 0x24a | Status_PDC | 8 | 0 |
| 587 | 0x24b | Status_door_sensors | 8 | 0 |
| 594 | 0x252 | Wiper_status | 8 | 0 |
| 598 | 0x256 | Challenge_Passive_Access | 8 | 0 |
| 600 | 0x258 | Status_Transmission_Passive_Access | 8 | 0 |
| 604 | 0x25c | Operation_of_climate_additional_programs | 8 | 0 |
| 621 | 0x26d | Operation_blinds_MK | 8 | 0 |
| 622 | 0x26e | Control_FH_SHD_central_comfort | 8 | 0 |
| 635 | 0x27b | Status_Shiftlights | 8 | 0 |
| 637 | 0x27d | Status_convertible_top_manual_convertible | 8 | 0 |
| 638 | 0x27e | Status_convertible_top_convertible | 8 | 0 |
| 639 | 0x27f | Status_central_locking_convertible_top | 8 | 0 |
| 642 | 0x282 | Control_security_vehicle_2 | 8 | 0 |
| 644 | 0x284 | Control_remote_start_safety_vehicle | 8 | 0 |
| 646 | 0x286 | Electrochromic_control | 8 | 0 |
| 652 | 0x28c | Pushbutton_vertical_dynamics | 8 | 0 |
| 653 | 0x28d | Operation_pushbutton_sport | 8 | 0 |
| 656 | 0x290 | Control_response_hydrogen_vehicle | 8 | 0 |
| 658 | 0x292 | Control_high_beam_assistant | 8 | 0 |
| 670 | 0x29e | Central_locking_control_for_security_vehicle | 8 | 0 |
| 671 | 0x29f | Remote_control_FondCommander | 8 | 0 |
| 672 | 0x2a0 | Central_locking_control | 8 | 0 |
| 674 | 0x2a2 | Operation_of_climate_stand_functions | 8 | 0 |
| 676 | 0x2a4 | Operation_personalization | 8 | 0 |
| 692 | 0x2b4 | DWA_Alarm | 8 | 0 |
| 694 | 0x2b6 | Control_horn_DWA | 8 | 0 |
| 696 | 0x2b8 | Operation_onboard_computer | 8 | 0 |
| 697 | 0x2b9 | Operation_RSE | 8 | 0 |
| 698 | 0x2ba | Stopwatch | 8 | 0 |
| 701 | 0x2bd | Request_switching_display | 8 | 0 |
| 702 | 0x2be | Switch_status_display | 8 | 0 |
| 703 | 0x2bf | Water_valve_control | 8 | 0 |
| 706 | 0x2c2 | Temperatur_Ist_Fond | 8 | 0 |
| 711 | 0x2c7 | Display_Kombination_extended | 8 | 0 |
| 714 | 0x2ca | Outside_temperature | 8 | 0 |
| 716 | 0x2cc | Control_monitor_rear | 8 | 0 |
| 718 | 0x2ce | Control_monitor | 8 | 0 |
| 719 | 0x2cf | Status_of_auxiliary_water_pump | 8 | 0 |
| 720 | 0x2d0 | Status_Sensor_AUC | 8 | 0 |
| 721 | 0x2d1 | Status_fitting_window_V | 8 | 0 |
| 722 | 0x2d2 | Status_pressure_refrigeration_circuit | 8 | 0 |
| 723 | 0x2d3 | Status_stratification_rear | 8 | 0 |
| 725 | 0x2d5 | Status_heating_rear_window | 8 | 0 |
| 726 | 0x2d6 | Status_valve_air_conditioning_compressor | 8 | 0 |
| 730 | 0x2da | Status_tailgate_lift | 8 | 0 |
| 734 | 0x2de | Switch_control_display | 8 | 0 |
| 738 | 0x2e2 | Status_setting_video_night_vision | 8 | 0 |
| 739 | 0x2e3 | Status_setting_video_rear_view_camera | 8 | 0 |
| 740 | 0x2e4 | Status_trailer | 8 | 0 |
| 742 | 0x2e6 | Status_of_air_distribution_FA | 8 | 0 |
| 746 | 0x2ea | Status_air_distribution_BF | 8 | 0 |
| 750 | 0x2ee | Status_climate_additional_programs | 8 | 0 |
| 752 | 0x2f0 | Status_air_condition_functions | 8 | 0 |
| 753 | 0x2f1 | Status_driver_detection | 8 | 0 |
| 755 | 0x2f3 | Display_switching_instruction | 8 | 0 |
| 756 | 0x2f4 | Air_conditioning_control_SH_ZH_auxiliary_water_pump | 8 | 0 |
| 759 | 0x2f7 | Units | 8 | 0 |
| 768 | 0x300 | Status_RSE | 8 | 0 |
| 772 | 0x304 | Status_Gang | 8 | 0 |
| 773 | 0x305 | Operation_button_convertible_top | 8 | 0 |
| 774 | 0x306 | Vehicle_tilt | 8 | 0 |
| 775 | 0x307 | Operation_button_flap_convertible_top | 8 | 0 |
| 776 | 0x308 | Status_MSA | 8 | 0 |
| 785 | 0x311 | Refill_quantity | 8 | 0 |
| 786 | 0x312 | Service_Call_Teleservice | 8 | 0 |
| 787 | 0x313 | Status_Service_Call_Teleservice | 8 | 0 |
| 788 | 0x314 | Status_driving_light | 8 | 0 |
| 789 | 0x315 | Vehicle_mode | 8 | 0 |
| 791 | 0x317 | Operation_button_parking_aids | 8 | 0 |
| 792 | 0x318 | Status_antennas_Passive_Access | 8 | 0 |
| 793 | 0x319 | Operation_push_button_RDC | 8 | 0 |
| 794 | 0x31a | Operation_button_HDC | 8 | 0 |
| 795 | 0x31b | Operation_of_tailgate_interior_button | 8 | 0 |
| 796 | 0x31c | Status_tire_pressure | 8 | 0 |
| 801 | 0x321 | Operation_button_camera_BF | 8 | 0 |
| 802 | 0x322 | Damper_current | 8 | 0 |
| 806 | 0x326 | Status_damper_program | 8 | 0 |
| 808 | 0x328 | Relativzeit | 8 | 0 |
| 813 | 0x32d | Display_HDC | 8 | 0 |
| 814 | 0x32e | Status_climate_internal_control_info | 8 | 0 |
| 817 | 0x331 | Programming_of_step_cruise_control | 8 | 0 |
| 818 | 0x332 | Driver_display_speed_range | 8 | 0 |
| 822 | 0x336 | Display_check_control_message_role | 8 | 0 |
| 824 | 0x338 | Control_display_check_control_message | 8 | 0 |
| 825 | 0x339 | Status_display_climate | 8 | 0 |
| 826 | 0x33a | Status_Monitor_Front | 8 | 0 |
| 828 | 0x33c | Status_Monitor_Fond_1 | 8 | 0 |
| 830 | 0x33e | Status_Monitor_Fond_2 | 8 | 0 |
| 841 | 0x349 | Raw_data_level_tank | 8 | 0 |
| 843 | 0x34b | Seat_back_lock_status_FA | 8 | 0 |
| 845 | 0x34d | Status_seat_back_lock_BF | 8 | 0 |
| 847 | 0x34f | Status_contact_handbrake | 8 | 1 |
| 858 | 0x35a | Appointment_Condition_Based_Service | 8 | 0 |
| 860 | 0x35c | Status_onboard_computer | 8 | 0 |
| 862 | 0x35e | Onboard_computer_data_trip_data | 8 | 0 |
| 864 | 0x360 | Data_onboard_computer_start_of_journey | 8 | 0 |
| 866 | 0x362 | Data_onboard_computer_average_values | 8 | 0 |
| 868 | 0x364 | Data_onboard_computer_arrival | 8 | 0 |
| 869 | 0x365 | Status_terminal_request | 8 | 0 |
| 870 | 0x366 | Display_Kombination_external_display | 8 | 0 |
| 871 | 0x367 | Control_display_of_demand_oriented_service | 8 | 0 |
| 877 | 0x36d | Setting_the_driving_dynamics_switch | 8 | 0 |
| 886 | 0x376 | Status_wear_lamella | 8 | 0 |
| 893 | 0x37d | Status_DKG | 8 | 0 |
| 894 | 0x37e | Temperatur_Bremse | 8 | 0 |
| 895 | 0x37f | Range_of_diesel_exhaust_gas_additive | 8 | 0 |
| 896 | 0x380 | chassis_number | 8 | 0 |
| 898 | 0x382 | Electronic_engine_oil_dipstick_M | 8 | 0 |
| 899 | 0x383 | Motor_data_2 | 8 | 0 |
| 904 | 0x388 | Vehicle_type | 8 | 0 |
| 907 | 0x38b | Status_battery | 8 | 0 |
| 910 | 0x38e | Start_speed | 8 | 0 |
| 914 | 0x392 | Status_System_AFS | 8 | 0 |
| 916 | 0x394 | RDA_request_data_storage | 8 | 0 |
| 917 | 0x395 | Coding_power_management | 8 | 0 |
| 920 | 0x398 | Operation_chassis | 8 | 0 |
| 921 | 0x399 | Status_MDrive | 6 | 0 |
| 926 | 0x39e | Operation_time_date | 8 | 0 |
| 928 | 0x3a0 | Vehicle_state | 8 | 0 |
| 931 | 0x3a3 | Request_Remote_Services | 8 | 0 |
| 937 | 0x3a9 | Status_motor_control_CKM | 8 | 0 |
| 939 | 0x3ab | Status_Shiftlights_CKM | 8 | 0 |
| 944 | 0x3b0 | Status_gear_reverse | 8 | 0 |
| 949 | 0x3b5 | Status_water_valve | 8 | 0 |
| 950 | 0x3b6 | Position_window_lifter_FAT | 8 | 0 |
| 951 | 0x3b7 | Position_window_lifter_FATH | 8 | 0 |
| 952 | 0x3b8 | Position_window_regulator_BFT | 8 | 0 |
| 953 | 0x3b9 | Position_window_regulator_BFTH | 8 | 0 |
| 954 | 0x3ba | Position_SHD | 8 | 0 |
| 956 | 0x3bc | Position_window_lifter_security_vehicle | 8 | 0 |
| 957 | 0x3bd | Status_consumer_shutdown | 8 | 0 |
| 959 | 0x3bf | Position_window_rear_window | 8 | 0 |
| 960 | 0x3c0 | Configuration_FAS | 8 | 0 |
| 961 | 0x3c1 | Configuration_BFS | 8 | 0 |
| 964 | 0x3c4 | Status_EDCK_CKM | 8 | 0 |
| 967 | 0x3c7 | Access_radio | 8 | 0 |
| 968 | 0x3c8 | Operation_push_button_radio | 8 | 0 |
| 974 | 0x3ce | Radio_audio_control_interface_display | 8 | 0 |
| 975 | 0x3cf | Acknowledgment_access_radio_audio_control_interface | 8 | 0 |
| 979 | 0x3d3 | Status_solar_sensor | 8 | 0 |
| 980 | 0x3d4 | Configuration_of_central_locking_CKM | 8 | 0 |
| 981 | 0x3d5 | Status_central_locking_CKM | 8 | 0 |
| 982 | 0x3d6 | Configuration_DWA_CKM | 8 | 0 |
| 983 | 0x3d7 | Status_DWA_CKM | 8 | 0 |
| 984 | 0x3d8 | Configuration_RLS_CKM | 8 | 0 |
| 985 | 0x3d9 | Status_RLS_CKM | 8 | 0 |
| 986 | 0x3da | Configuration_of_memory_positions_CKM | 8 | 0 |
| 987 | 0x3db | Status_memory_positions_CKM | 8 | 0 |
| 988 | 0x3dc | Configuration_light_CKM | 8 | 0 |
| 989 | 0x3dd | Status_light_CKM | 8 | 0 |
| 990 | 0x3de | Configuration_Climate_CKM | 8 | 0 |
| 991 | 0x3df | Status_Klima_CKM | 8 | 0 |
| 994 | 0x3e2 | Configuration_of_tailgate_CKM | 8 | 0 |
| 995 | 0x3e3 | Status_tailgate_CKM | 8 | 0 |
| 996 | 0x3e4 | Configuration_rear_view_camera_CKM | 8 | 0 |

## mercedes_benz_e350_2010 — Mercedes W212 [B]

- Make: mercedes; E350 2010 (W212)
- Messages: 16; signals: 97
- Evidence: opendbc/opendbc/dbc/mercedes_benz_e350_2010.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 3 | 0x3 | STEER_SENSOR | 8 | 5 |
| 5 | 0x5 | BRAKE_MODULE | 8 | 7 |
| 69 | 0x45 | DRIVER_CONTROLS | 8 | 14 |
| 513 | 0x201 | WHEEL_ENCODERS | 8 | 6 |
| 261 | 0x105 | GAS_PEDAL | 8 | 5 |
| 643 | 0x283 | DOOR_SENSORS | 8 | 9 |
| 885 | 0x375 | SEATBELT_SENSORS | 8 | 2 |
| 257 | 0x101 | CRUISE_CONTROL | 8 | 10 |
| 260 | 0x104 | CRUISE_CONTROL2 | 8 | 7 |
| 14 | 0xe | STEER_TORQUE | 8 | 3 |
| 888 | 0x378 | CRUISE_CONTROL3 | 8 | 11 |
| 307 | 0x133 | POWER_SEATS | 8 | 2 |
| 109 | 0x6d | GEAR_LEVER | 8 | 7 |
| 115 | 0x73 | GEAR_PACKET | 8 | 1 |
| 581 | 0x245 | IGNITION | 8 | 0 |
| 515 | 0x203 | WHEEL_SPEEDS | 8 | 8 |

## volvo_v40_2017_pt — Volvo V40 [B]

- Make: volvo; V40 2017 powertrain bus
- Messages: 51; signals: 165
- Evidence: opendbc/opendbc/dbc/volvo_v40_2017_pt.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 8 | 0x8 | SAS0 | 8 | 6 |
| 16 | 0x10 | CCButtons | 8 | 18 |
| 48 | 0x30 | FSM0 | 8 | 5 |
| 64 | 0x40 | TCM0 | 8 | 2 |
| 85 | 0x55 | PedalandBrake | 8 | 6 |
| 101 | 0x65 | EngineInfo | 8 | 2 |
| 112 | 0x70 | NEW_MSG_4 | 8 | 1 |
| 114 | 0x72 | ECM1 | 8 | 7 |
| 117 | 0x75 | ECM1_2 | 8 | 0 |
| 128 | 0x80 | NEW_MSG_5 | 8 | 2 |
| 176 | 0xb0 | ECM2 | 8 | 2 |
| 192 | 0xc0 | Gear | 8 | 1 |
| 208 | 0xd0 | FSM1 | 8 | 9 |
| 224 | 0xe0 | PSCM0 | 8 | 6 |
| 245 | 0xf5 | wheelspeed0 | 8 | 4 |
| 272 | 0x110 | SpeedSignal0 | 8 | 1 |
| 288 | 0x120 | wheel_speed1 | 8 | 2 |
| 293 | 0x125 | PSCM1 | 8 | 7 |
| 304 | 0x130 | VehicleSpeed0 | 8 | 3 |
| 325 | 0x145 | ECM3 | 8 | 0 |
| 336 | 0x150 | VehicleSpeed1 | 8 | 3 |
| 352 | 0x160 | FSM2 | 8 | 5 |
| 432 | 0x1b0 | BrakeMessages | 8 | 3 |
| 464 | 0x1d0 | DIM0 | 8 | 0 |
| 480 | 0x1e0 | BCM0 | 8 | 0 |
| 528 | 0x210 | CEM0 | 8 | 0 |
| 608 | 0x260 | CVM0 | 8 | 3 |
| 624 | 0x270 | FSM3 | 8 | 1 |
| 640 | 0x280 | FSM4 | 8 | 2 |
| 648 | 0x288 | SRS0 | 8 | 0 |
| 652 | 0x28c | ECM4 | 8 | 0 |
| 656 | 0x290 | ECM5 | 8 | 0 |
| 657 | 0x291 | ECM6 | 8 | 0 |
| 681 | 0x2a9 | MiscCarInfo | 8 | 2 |
| 693 | 0x2b5 | ECM7 | 8 | 0 |
| 709 | 0x2c5 | ACC | 8 | 1 |
| 853 | 0x355 | FSM5 | 8 | 10 |
| 864 | 0x360 | CEM1 | 8 | 0 |
| 912 | 0x390 | DIM1 | 8 | 0 |
| 968 | 0x3c8 | SRS1 | 8 | 2 |
| 1029 | 0x405 | CEMBCM0 | 8 | 0 |
| 1344 | 0x540 | NEW_MSG_1 | 8 | 1 |
| 1830 | 0x726 | diagCEMReq | 8 | 8 |
| 1838 | 0x72e | diagCEMResp | 8 | 2 |
| 1840 | 0x730 | diagPSCMReq | 8 | 8 |
| 1848 | 0x738 | diagPSCMResp | 8 | 2 |
| 1892 | 0x764 | diagFSMReq | 8 | 8 |
| 1900 | 0x76c | diagFSMResp | 8 | 2 |
| 1939 | 0x793 | diagCVMReq | 8 | 8 |
| 1947 | 0x79b | diagCVMResp | 8 | 2 |
| 2015 | 0x7df | diagGlobalReq | 8 | 8 |

## volvo_v60_2015_pt — Volvo V60 [B]

- Make: volvo; V60 2015 powertrain bus
- Messages: 41; signals: 147
- Evidence: opendbc/opendbc/dbc/volvo_v60_2015_pt.dbc (commaai/opendbc @ a7da786, shallow clone 2026-10-06)

| ID (dec) | ID (hex) | Name | DLC | Signals |
|---|---|---|---|---|
| 16 | 0x10 | SAS0 | 8 | 6 |
| 32 | 0x20 | AccPedal | 8 | 1 |
| 81 | 0x51 | FSM0 | 8 | 1 |
| 277 | 0x115 | NEW_MSG_7 | 8 | 1 |
| 295 | 0x127 | CCButtons | 8 | 12 |
| 298 | 0x12a | EngineData | 8 | 10 |
| 307 | 0x133 | NEW_MSG_133 | 8 | 1 |
| 328 | 0x148 | VehicleSpeed1 | 8 | 3 |
| 336 | 0x150 | NEW_MSG_8 | 8 | 4 |
| 359 | 0x167 | ACC_Speed | 8 | 3 |
| 384 | 0x180 | Accessories_02 | 8 | 2 |
| 465 | 0x1d1 | NEW_MSG_4 | 8 | 2 |
| 522 | 0x20a | Brake_Info | 8 | 8 |
| 544 | 0x220 | wheelspeed1 | 8 | 2 |
| 565 | 0x235 | wheelspeed0 | 8 | 2 |
| 582 | 0x246 | PSCM1 | 8 | 7 |
| 608 | 0x260 | FSM1 | 8 | 1 |
| 609 | 0x261 | fromWhere | 8 | 3 |
| 610 | 0x262 | FSM2 | 8 | 8 |
| 612 | 0x264 | Accessories_03 | 8 | 1 |
| 624 | 0x270 | FSM3 | 8 | 5 |
| 648 | 0x288 | BrakePedal | 8 | 2 |
| 750 | 0x2ee | HandBrake | 8 | 2 |
| 794 | 0x31a | FSM4 | 8 | 3 |
| 802 | 0x322 | StartStop | 8 | 1 |
| 923 | 0x39b | Accessories_01 | 8 | 2 |
| 1006 | 0x3ee | Doors | 8 | 2 |
| 1021 | 0x3fd | FSM5 | 8 | 1 |
| 1024 | 0x400 | NEW_MSG_400 | 8 | 1 |
| 1039 | 0x40f | MiscCarInfo | 8 | 1 |
| 1174 | 0x496 | Lights | 8 | 1 |
| 1279 | 0x4ff | PSCM3 | 8 | 0 |
| 1830 | 0x726 | diagCEMReq | 8 | 8 |
| 1838 | 0x72e | diagCEMResp | 8 | 2 |
| 1840 | 0x730 | diagPSCMReq | 8 | 8 |
| 1848 | 0x738 | diagPSCMResp | 8 | 2 |
| 1892 | 0x764 | diagFSMReq | 8 | 8 |
| 1900 | 0x76c | diagFSMResp | 8 | 2 |
| 1939 | 0x793 | diagCVMReq | 8 | 8 |
| 1947 | 0x79b | diagCVMResp | 8 | 2 |
| 2015 | 0x7df | diagGlobalReq | 8 | 8 |

_Generated by scripts/build.py — do not hand-edit._
