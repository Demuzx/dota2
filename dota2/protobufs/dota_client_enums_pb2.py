# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dota_client_enums.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dota_client_enums.proto',
  package='dota',
  syntax='proto2',
  serialized_pb=_b('\n\x17\x64ota_client_enums.proto\x12\x04\x64ota*^\n\x13\x45TournamentTemplate\x12\x1e\n\x1ak_ETournamentTemplate_None\x10\x00\x12\'\n#k_ETournamentTemplate_AutomatedWin3\x10\x01*\xa8\x03\n\x14\x45TournamentGameState\x12\"\n\x1ek_ETournamentGameState_Unknown\x10\x00\x12#\n\x1fk_ETournamentGameState_Canceled\x10\x01\x12$\n k_ETournamentGameState_Scheduled\x10\x02\x12!\n\x1dk_ETournamentGameState_Active\x10\x03\x12%\n!k_ETournamentGameState_RadVictory\x10\x14\x12&\n\"k_ETournamentGameState_DireVictory\x10\x15\x12.\n*k_ETournamentGameState_RadVictoryByForfeit\x10\x16\x12/\n+k_ETournamentGameState_DireVictoryByForfeit\x10\x17\x12(\n$k_ETournamentGameState_ServerFailure\x10(\x12$\n k_ETournamentGameState_NotNeeded\x10)*\xe7\x06\n\x14\x45TournamentTeamState\x12\"\n\x1ek_ETournamentTeamState_Unknown\x10\x00\x12 \n\x1ck_ETournamentTeamState_Node1\x10\x01\x12#\n\x1ek_ETournamentTeamState_NodeMax\x10\x80\x08\x12&\n!k_ETournamentTeamState_Eliminated\x10\xb3m\x12%\n k_ETournamentTeamState_Forfeited\x10\xb4m\x12\'\n\"k_ETournamentTeamState_Finished1st\x10\x99u\x12\'\n\"k_ETournamentTeamState_Finished2nd\x10\x9au\x12\'\n\"k_ETournamentTeamState_Finished3rd\x10\x9bu\x12\'\n\"k_ETournamentTeamState_Finished4th\x10\x9cu\x12\'\n\"k_ETournamentTeamState_Finished5th\x10\x9du\x12\'\n\"k_ETournamentTeamState_Finished6th\x10\x9eu\x12\'\n\"k_ETournamentTeamState_Finished7th\x10\x9fu\x12\'\n\"k_ETournamentTeamState_Finished8th\x10\xa0u\x12\'\n\"k_ETournamentTeamState_Finished9th\x10\xa1u\x12(\n#k_ETournamentTeamState_Finished10th\x10\xa2u\x12(\n#k_ETournamentTeamState_Finished11th\x10\xa3u\x12(\n#k_ETournamentTeamState_Finished12th\x10\xa4u\x12(\n#k_ETournamentTeamState_Finished13th\x10\xa5u\x12(\n#k_ETournamentTeamState_Finished14th\x10\xa6u\x12(\n#k_ETournamentTeamState_Finished15th\x10\xa7u\x12(\n#k_ETournamentTeamState_Finished16th\x10\xa8u*\x86\x03\n\x10\x45TournamentState\x12\x1e\n\x1ak_ETournamentState_Unknown\x10\x00\x12&\n\"k_ETournamentState_CanceledByAdmin\x10\x01\x12 \n\x1ck_ETournamentState_Completed\x10\x02\x12\x1d\n\x19k_ETournamentState_Merged\x10\x03\x12$\n k_ETournamentState_ServerFailure\x10\x04\x12$\n k_ETournamentState_TeamAbandoned\x10\x05\x12)\n%k_ETournamentState_TeamTimeoutForfeit\x10\x06\x12(\n$k_ETournamentState_TeamTimeoutRefund\x10\x07\x12!\n\x1dk_ETournamentState_InProgress\x10\x64\x12%\n!k_ETournamentState_WaitingToMerge\x10\x65*\xcc\x04\n\x14\x45TournamentNodeState\x12\"\n\x1ek_ETournamentNodeState_Unknown\x10\x00\x12#\n\x1fk_ETournamentNodeState_Canceled\x10\x01\x12.\n*k_ETournamentNodeState_TeamsNotYetAssigned\x10\x02\x12)\n%k_ETournamentNodeState_InBetweenGames\x10\x03\x12)\n%k_ETournamentNodeState_GameInProgress\x10\x04\x12 \n\x1ck_ETournamentNodeState_A_Won\x10\x05\x12 \n\x1ck_ETournamentNodeState_B_Won\x10\x06\x12)\n%k_ETournamentNodeState_A_WonByForfeit\x10\x07\x12)\n%k_ETournamentNodeState_B_WonByForfeit\x10\x08\x12 \n\x1ck_ETournamentNodeState_A_Bye\x10\t\x12&\n\"k_ETournamentNodeState_A_Abandoned\x10\n\x12(\n$k_ETournamentNodeState_ServerFailure\x10\x0b\x12+\n\'k_ETournamentNodeState_A_TimeoutForfeit\x10\x0c\x12*\n&k_ETournamentNodeState_A_TimeoutRefund\x10\r*\xc7\x03\n\x15\x45\x44OTAGroupMergeResult\x12\x1e\n\x1ak_EDOTAGroupMergeResult_OK\x10\x00\x12*\n&k_EDOTAGroupMergeResult_FAILED_GENERIC\x10\x01\x12&\n\"k_EDOTAGroupMergeResult_NOT_LEADER\x10\x02\x12,\n(k_EDOTAGroupMergeResult_TOO_MANY_PLAYERS\x10\x03\x12,\n(k_EDOTAGroupMergeResult_TOO_MANY_COACHES\x10\x04\x12+\n\'k_EDOTAGroupMergeResult_ENGINE_MISMATCH\x10\x05\x12)\n%k_EDOTAGroupMergeResult_NO_SUCH_GROUP\x10\x06\x12\x30\n,k_EDOTAGroupMergeResult_OTHER_GROUP_NOT_OPEN\x10\x07\x12+\n\'k_EDOTAGroupMergeResult_ALREADY_INVITED\x10\x08\x12\'\n#k_EDOTAGroupMergeResult_NOT_INVITED\x10\tB\x05H\x01\x90\x01\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ETOURNAMENTTEMPLATE = _descriptor.EnumDescriptor(
  name='ETournamentTemplate',
  full_name='dota.ETournamentTemplate',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTemplate_None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTemplate_AutomatedWin3', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=33,
  serialized_end=127,
)
_sym_db.RegisterEnumDescriptor(_ETOURNAMENTTEMPLATE)

ETournamentTemplate = enum_type_wrapper.EnumTypeWrapper(_ETOURNAMENTTEMPLATE)
_ETOURNAMENTGAMESTATE = _descriptor.EnumDescriptor(
  name='ETournamentGameState',
  full_name='dota.ETournamentGameState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_Canceled', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_Scheduled', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_Active', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_RadVictory', index=4, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_DireVictory', index=5, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_RadVictoryByForfeit', index=6, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_DireVictoryByForfeit', index=7, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_ServerFailure', index=8, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentGameState_NotNeeded', index=9, number=41,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=130,
  serialized_end=554,
)
_sym_db.RegisterEnumDescriptor(_ETOURNAMENTGAMESTATE)

ETournamentGameState = enum_type_wrapper.EnumTypeWrapper(_ETOURNAMENTGAMESTATE)
_ETOURNAMENTTEAMSTATE = _descriptor.EnumDescriptor(
  name='ETournamentTeamState',
  full_name='dota.ETournamentTeamState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Node1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_NodeMax', index=2, number=1024,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Eliminated', index=3, number=14003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Forfeited', index=4, number=14004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished1st', index=5, number=15001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished2nd', index=6, number=15002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished3rd', index=7, number=15003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished4th', index=8, number=15004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished5th', index=9, number=15005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished6th', index=10, number=15006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished7th', index=11, number=15007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished8th', index=12, number=15008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished9th', index=13, number=15009,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished10th', index=14, number=15010,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished11th', index=15, number=15011,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished12th', index=16, number=15012,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished13th', index=17, number=15013,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished14th', index=18, number=15014,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished15th', index=19, number=15015,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentTeamState_Finished16th', index=20, number=15016,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=557,
  serialized_end=1428,
)
_sym_db.RegisterEnumDescriptor(_ETOURNAMENTTEAMSTATE)

ETournamentTeamState = enum_type_wrapper.EnumTypeWrapper(_ETOURNAMENTTEAMSTATE)
_ETOURNAMENTSTATE = _descriptor.EnumDescriptor(
  name='ETournamentState',
  full_name='dota.ETournamentState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_CanceledByAdmin', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_Completed', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_Merged', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_ServerFailure', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_TeamAbandoned', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_TeamTimeoutForfeit', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_TeamTimeoutRefund', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_InProgress', index=8, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentState_WaitingToMerge', index=9, number=101,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1431,
  serialized_end=1821,
)
_sym_db.RegisterEnumDescriptor(_ETOURNAMENTSTATE)

ETournamentState = enum_type_wrapper.EnumTypeWrapper(_ETOURNAMENTSTATE)
_ETOURNAMENTNODESTATE = _descriptor.EnumDescriptor(
  name='ETournamentNodeState',
  full_name='dota.ETournamentNodeState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_Canceled', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_TeamsNotYetAssigned', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_InBetweenGames', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_GameInProgress', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_A_Won', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_B_Won', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_A_WonByForfeit', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_B_WonByForfeit', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_A_Bye', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_A_Abandoned', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_ServerFailure', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_A_TimeoutForfeit', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_ETournamentNodeState_A_TimeoutRefund', index=13, number=13,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1824,
  serialized_end=2412,
)
_sym_db.RegisterEnumDescriptor(_ETOURNAMENTNODESTATE)

ETournamentNodeState = enum_type_wrapper.EnumTypeWrapper(_ETOURNAMENTNODESTATE)
_EDOTAGROUPMERGERESULT = _descriptor.EnumDescriptor(
  name='EDOTAGroupMergeResult',
  full_name='dota.EDOTAGroupMergeResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_FAILED_GENERIC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_NOT_LEADER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_TOO_MANY_PLAYERS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_TOO_MANY_COACHES', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_ENGINE_MISMATCH', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_NO_SUCH_GROUP', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_OTHER_GROUP_NOT_OPEN', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_ALREADY_INVITED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTAGroupMergeResult_NOT_INVITED', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2415,
  serialized_end=2870,
)
_sym_db.RegisterEnumDescriptor(_EDOTAGROUPMERGERESULT)

EDOTAGroupMergeResult = enum_type_wrapper.EnumTypeWrapper(_EDOTAGROUPMERGERESULT)
k_ETournamentTemplate_None = 0
k_ETournamentTemplate_AutomatedWin3 = 1
k_ETournamentGameState_Unknown = 0
k_ETournamentGameState_Canceled = 1
k_ETournamentGameState_Scheduled = 2
k_ETournamentGameState_Active = 3
k_ETournamentGameState_RadVictory = 20
k_ETournamentGameState_DireVictory = 21
k_ETournamentGameState_RadVictoryByForfeit = 22
k_ETournamentGameState_DireVictoryByForfeit = 23
k_ETournamentGameState_ServerFailure = 40
k_ETournamentGameState_NotNeeded = 41
k_ETournamentTeamState_Unknown = 0
k_ETournamentTeamState_Node1 = 1
k_ETournamentTeamState_NodeMax = 1024
k_ETournamentTeamState_Eliminated = 14003
k_ETournamentTeamState_Forfeited = 14004
k_ETournamentTeamState_Finished1st = 15001
k_ETournamentTeamState_Finished2nd = 15002
k_ETournamentTeamState_Finished3rd = 15003
k_ETournamentTeamState_Finished4th = 15004
k_ETournamentTeamState_Finished5th = 15005
k_ETournamentTeamState_Finished6th = 15006
k_ETournamentTeamState_Finished7th = 15007
k_ETournamentTeamState_Finished8th = 15008
k_ETournamentTeamState_Finished9th = 15009
k_ETournamentTeamState_Finished10th = 15010
k_ETournamentTeamState_Finished11th = 15011
k_ETournamentTeamState_Finished12th = 15012
k_ETournamentTeamState_Finished13th = 15013
k_ETournamentTeamState_Finished14th = 15014
k_ETournamentTeamState_Finished15th = 15015
k_ETournamentTeamState_Finished16th = 15016
k_ETournamentState_Unknown = 0
k_ETournamentState_CanceledByAdmin = 1
k_ETournamentState_Completed = 2
k_ETournamentState_Merged = 3
k_ETournamentState_ServerFailure = 4
k_ETournamentState_TeamAbandoned = 5
k_ETournamentState_TeamTimeoutForfeit = 6
k_ETournamentState_TeamTimeoutRefund = 7
k_ETournamentState_InProgress = 100
k_ETournamentState_WaitingToMerge = 101
k_ETournamentNodeState_Unknown = 0
k_ETournamentNodeState_Canceled = 1
k_ETournamentNodeState_TeamsNotYetAssigned = 2
k_ETournamentNodeState_InBetweenGames = 3
k_ETournamentNodeState_GameInProgress = 4
k_ETournamentNodeState_A_Won = 5
k_ETournamentNodeState_B_Won = 6
k_ETournamentNodeState_A_WonByForfeit = 7
k_ETournamentNodeState_B_WonByForfeit = 8
k_ETournamentNodeState_A_Bye = 9
k_ETournamentNodeState_A_Abandoned = 10
k_ETournamentNodeState_ServerFailure = 11
k_ETournamentNodeState_A_TimeoutForfeit = 12
k_ETournamentNodeState_A_TimeoutRefund = 13
k_EDOTAGroupMergeResult_OK = 0
k_EDOTAGroupMergeResult_FAILED_GENERIC = 1
k_EDOTAGroupMergeResult_NOT_LEADER = 2
k_EDOTAGroupMergeResult_TOO_MANY_PLAYERS = 3
k_EDOTAGroupMergeResult_TOO_MANY_COACHES = 4
k_EDOTAGroupMergeResult_ENGINE_MISMATCH = 5
k_EDOTAGroupMergeResult_NO_SUCH_GROUP = 6
k_EDOTAGroupMergeResult_OTHER_GROUP_NOT_OPEN = 7
k_EDOTAGroupMergeResult_ALREADY_INVITED = 8
k_EDOTAGroupMergeResult_NOT_INVITED = 9


DESCRIPTOR.enum_types_by_name['ETournamentTemplate'] = _ETOURNAMENTTEMPLATE
DESCRIPTOR.enum_types_by_name['ETournamentGameState'] = _ETOURNAMENTGAMESTATE
DESCRIPTOR.enum_types_by_name['ETournamentTeamState'] = _ETOURNAMENTTEAMSTATE
DESCRIPTOR.enum_types_by_name['ETournamentState'] = _ETOURNAMENTSTATE
DESCRIPTOR.enum_types_by_name['ETournamentNodeState'] = _ETOURNAMENTNODESTATE
DESCRIPTOR.enum_types_by_name['EDOTAGroupMergeResult'] = _EDOTAGROUPMERGERESULT


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001\220\001\000'))
# @@protoc_insertion_point(module_scope)
