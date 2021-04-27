# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nuance/rpc/error_details.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nuance/rpc/error_details.proto',
  package='nuance.rpc',
  syntax='proto3',
  serialized_options=b'\n\016com.nuance.rpcP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1enuance/rpc/error_details.proto\x12\nnuance.rpc\"#\n\tRetryInfo\x12\x16\n\x0eretry_delay_ms\x18\x01 \x01(\x05\"\xca\x01\n\x0bRequestInfo\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x14\n\x0crequest_data\x18\x02 \x01(\t\x12S\n\x17\x61\x64\x64itional_request_data\x18\x03 \x03(\x0b\x32\x32.nuance.rpc.RequestInfo.AdditionalRequestDataEntry\x1a<\n\x1a\x41\x64\x64itionalRequestDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x86\x01\n\x08HelpInfo\x12-\n\x05links\x18\x01 \x03(\x0b\x32\x1e.nuance.rpc.HelpInfo.Hyperlink\x1aK\n\tHyperlink\x12\x31\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32\x1c.nuance.rpc.LocalizedMessage\x12\x0b\n\x03url\x18\x02 \x01(\t\"P\n\x10LocalizedMessage\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x1b\n\x13message_resource_id\x18\x03 \x01(\t\"\xed\x02\n\x0e\x46ieldViolation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x11\n\trel_field\x18\x02 \x03(\t\x12\x32\n\x0cuser_message\x18\x03 \x01(\x0b\x32\x1c.nuance.rpc.LocalizedMessage\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x15\n\rinvalid_value\x18\x05 \x01(\t\x12;\n\tviolation\x18\x06 \x01(\x0e\x32(.nuance.rpc.FieldViolation.ViolationType\"\x9f\x01\n\rViolationType\x12\x1b\n\x17MANDATORY_FIELD_MISSING\x10\x00\x12\x12\n\x0e\x46IELD_CONFLICT\x10\x01\x12\x10\n\x0cOUT_OF_RANGE\x10\x02\x12\x12\n\x0eINVALID_FORMAT\x10\x03\x12\r\n\tTOO_SHORT\x10\x04\x12\x0c\n\x08TOO_LONG\x10\x05\x12\t\n\x05OTHER\x10@\x12\x0f\n\x0bUNSPECIFIED\x10\x63\"\xb8\x01\n\x0cStatusDetail\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x32\n\x0cuser_message\x18\x02 \x01(\x0b\x32\x1c.nuance.rpc.LocalizedMessage\x12\x34\n\x06\x65xtras\x18\x03 \x03(\x0b\x32$.nuance.rpc.StatusDetail.ExtrasEntry\x1a-\n\x0b\x45xtrasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x12\n\x0e\x63om.nuance.rpcP\x01\x62\x06proto3'
)



_FIELDVIOLATION_VIOLATIONTYPE = _descriptor.EnumDescriptor(
  name='ViolationType',
  full_name='nuance.rpc.FieldViolation.ViolationType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MANDATORY_FIELD_MISSING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIELD_CONFLICT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_RANGE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FORMAT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_SHORT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_LONG', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=6, number=64,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=7, number=99,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=714,
  serialized_end=873,
)
_sym_db.RegisterEnumDescriptor(_FIELDVIOLATION_VIOLATIONTYPE)


_RETRYINFO = _descriptor.Descriptor(
  name='RetryInfo',
  full_name='nuance.rpc.RetryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='retry_delay_ms', full_name='nuance.rpc.RetryInfo.retry_delay_ms', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=81,
)


_REQUESTINFO_ADDITIONALREQUESTDATAENTRY = _descriptor.Descriptor(
  name='AdditionalRequestDataEntry',
  full_name='nuance.rpc.RequestInfo.AdditionalRequestDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='nuance.rpc.RequestInfo.AdditionalRequestDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='nuance.rpc.RequestInfo.AdditionalRequestDataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=286,
)

_REQUESTINFO = _descriptor.Descriptor(
  name='RequestInfo',
  full_name='nuance.rpc.RequestInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='nuance.rpc.RequestInfo.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_data', full_name='nuance.rpc.RequestInfo.request_data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='additional_request_data', full_name='nuance.rpc.RequestInfo.additional_request_data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTINFO_ADDITIONALREQUESTDATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=286,
)


_HELPINFO_HYPERLINK = _descriptor.Descriptor(
  name='Hyperlink',
  full_name='nuance.rpc.HelpInfo.Hyperlink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='nuance.rpc.HelpInfo.Hyperlink.description', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='nuance.rpc.HelpInfo.Hyperlink.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=423,
)

_HELPINFO = _descriptor.Descriptor(
  name='HelpInfo',
  full_name='nuance.rpc.HelpInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='links', full_name='nuance.rpc.HelpInfo.links', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HELPINFO_HYPERLINK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=423,
)


_LOCALIZEDMESSAGE = _descriptor.Descriptor(
  name='LocalizedMessage',
  full_name='nuance.rpc.LocalizedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locale', full_name='nuance.rpc.LocalizedMessage.locale', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='nuance.rpc.LocalizedMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_resource_id', full_name='nuance.rpc.LocalizedMessage.message_resource_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=505,
)


_FIELDVIOLATION = _descriptor.Descriptor(
  name='FieldViolation',
  full_name='nuance.rpc.FieldViolation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='nuance.rpc.FieldViolation.field', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rel_field', full_name='nuance.rpc.FieldViolation.rel_field', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_message', full_name='nuance.rpc.FieldViolation.user_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='nuance.rpc.FieldViolation.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invalid_value', full_name='nuance.rpc.FieldViolation.invalid_value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='violation', full_name='nuance.rpc.FieldViolation.violation', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIELDVIOLATION_VIOLATIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=873,
)


_STATUSDETAIL_EXTRASENTRY = _descriptor.Descriptor(
  name='ExtrasEntry',
  full_name='nuance.rpc.StatusDetail.ExtrasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='nuance.rpc.StatusDetail.ExtrasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='nuance.rpc.StatusDetail.ExtrasEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1015,
  serialized_end=1060,
)

_STATUSDETAIL = _descriptor.Descriptor(
  name='StatusDetail',
  full_name='nuance.rpc.StatusDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='nuance.rpc.StatusDetail.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_message', full_name='nuance.rpc.StatusDetail.user_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='nuance.rpc.StatusDetail.extras', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STATUSDETAIL_EXTRASENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=876,
  serialized_end=1060,
)

_REQUESTINFO_ADDITIONALREQUESTDATAENTRY.containing_type = _REQUESTINFO
_REQUESTINFO.fields_by_name['additional_request_data'].message_type = _REQUESTINFO_ADDITIONALREQUESTDATAENTRY
_HELPINFO_HYPERLINK.fields_by_name['description'].message_type = _LOCALIZEDMESSAGE
_HELPINFO_HYPERLINK.containing_type = _HELPINFO
_HELPINFO.fields_by_name['links'].message_type = _HELPINFO_HYPERLINK
_FIELDVIOLATION.fields_by_name['user_message'].message_type = _LOCALIZEDMESSAGE
_FIELDVIOLATION.fields_by_name['violation'].enum_type = _FIELDVIOLATION_VIOLATIONTYPE
_FIELDVIOLATION_VIOLATIONTYPE.containing_type = _FIELDVIOLATION
_STATUSDETAIL_EXTRASENTRY.containing_type = _STATUSDETAIL
_STATUSDETAIL.fields_by_name['user_message'].message_type = _LOCALIZEDMESSAGE
_STATUSDETAIL.fields_by_name['extras'].message_type = _STATUSDETAIL_EXTRASENTRY
DESCRIPTOR.message_types_by_name['RetryInfo'] = _RETRYINFO
DESCRIPTOR.message_types_by_name['RequestInfo'] = _REQUESTINFO
DESCRIPTOR.message_types_by_name['HelpInfo'] = _HELPINFO
DESCRIPTOR.message_types_by_name['LocalizedMessage'] = _LOCALIZEDMESSAGE
DESCRIPTOR.message_types_by_name['FieldViolation'] = _FIELDVIOLATION
DESCRIPTOR.message_types_by_name['StatusDetail'] = _STATUSDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetryInfo = _reflection.GeneratedProtocolMessageType('RetryInfo', (_message.Message,), {
  'DESCRIPTOR' : _RETRYINFO,
  '__module__' : 'nuance.rpc.error_details_pb2'
  # @@protoc_insertion_point(class_scope:nuance.rpc.RetryInfo)
  })
_sym_db.RegisterMessage(RetryInfo)

RequestInfo = _reflection.GeneratedProtocolMessageType('RequestInfo', (_message.Message,), {

  'AdditionalRequestDataEntry' : _reflection.GeneratedProtocolMessageType('AdditionalRequestDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUESTINFO_ADDITIONALREQUESTDATAENTRY,
    '__module__' : 'nuance.rpc.error_details_pb2'
    # @@protoc_insertion_point(class_scope:nuance.rpc.RequestInfo.AdditionalRequestDataEntry)
    })
  ,
  'DESCRIPTOR' : _REQUESTINFO,
  '__module__' : 'nuance.rpc.error_details_pb2'
  # @@protoc_insertion_point(class_scope:nuance.rpc.RequestInfo)
  })
_sym_db.RegisterMessage(RequestInfo)
_sym_db.RegisterMessage(RequestInfo.AdditionalRequestDataEntry)

HelpInfo = _reflection.GeneratedProtocolMessageType('HelpInfo', (_message.Message,), {

  'Hyperlink' : _reflection.GeneratedProtocolMessageType('Hyperlink', (_message.Message,), {
    'DESCRIPTOR' : _HELPINFO_HYPERLINK,
    '__module__' : 'nuance.rpc.error_details_pb2'
    # @@protoc_insertion_point(class_scope:nuance.rpc.HelpInfo.Hyperlink)
    })
  ,
  'DESCRIPTOR' : _HELPINFO,
  '__module__' : 'nuance.rpc.error_details_pb2'
  # @@protoc_insertion_point(class_scope:nuance.rpc.HelpInfo)
  })
_sym_db.RegisterMessage(HelpInfo)
_sym_db.RegisterMessage(HelpInfo.Hyperlink)

LocalizedMessage = _reflection.GeneratedProtocolMessageType('LocalizedMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCALIZEDMESSAGE,
  '__module__' : 'nuance.rpc.error_details_pb2'
  # @@protoc_insertion_point(class_scope:nuance.rpc.LocalizedMessage)
  })
_sym_db.RegisterMessage(LocalizedMessage)

FieldViolation = _reflection.GeneratedProtocolMessageType('FieldViolation', (_message.Message,), {
  'DESCRIPTOR' : _FIELDVIOLATION,
  '__module__' : 'nuance.rpc.error_details_pb2'
  # @@protoc_insertion_point(class_scope:nuance.rpc.FieldViolation)
  })
_sym_db.RegisterMessage(FieldViolation)

StatusDetail = _reflection.GeneratedProtocolMessageType('StatusDetail', (_message.Message,), {

  'ExtrasEntry' : _reflection.GeneratedProtocolMessageType('ExtrasEntry', (_message.Message,), {
    'DESCRIPTOR' : _STATUSDETAIL_EXTRASENTRY,
    '__module__' : 'nuance.rpc.error_details_pb2'
    # @@protoc_insertion_point(class_scope:nuance.rpc.StatusDetail.ExtrasEntry)
    })
  ,
  'DESCRIPTOR' : _STATUSDETAIL,
  '__module__' : 'nuance.rpc.error_details_pb2'
  # @@protoc_insertion_point(class_scope:nuance.rpc.StatusDetail)
  })
_sym_db.RegisterMessage(StatusDetail)
_sym_db.RegisterMessage(StatusDetail.ExtrasEntry)


DESCRIPTOR._options = None
_REQUESTINFO_ADDITIONALREQUESTDATAENTRY._options = None
_STATUSDETAIL_EXTRASENTRY._options = None
# @@protoc_insertion_point(module_scope)