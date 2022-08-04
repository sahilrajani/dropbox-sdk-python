# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# @generated
# flake8: noqa
# pylint: skip-file
from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class AuthError(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    invalid_token = None
    # Attribute is overwritten below the class definition
    no_openid_auth = None
    # Attribute is overwritten below the class definition
    other = None

    def is_invalid_token(self):
        """
        Check if the union tag is ``invalid_token``.

        :rtype: bool
        """
        return self._tag == 'invalid_token'

    def is_no_openid_auth(self):
        """
        Check if the union tag is ``no_openid_auth``.

        :rtype: bool
        """
        return self._tag == 'no_openid_auth'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(AuthError, self)._process_custom_annotations(annotation_type, field_path, processor)

AuthError_validator = bv.Union(AuthError)

class UserInfoArgs(bb.Struct):
    """
    This struct is empty. The comment here is intentionally emitted to avoid
    indentation issues with Stone.
    """

    __slots__ = [
    ]

    _has_required_fields = False

    def __init__(self):
        pass

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(UserInfoArgs, self)._process_custom_annotations(annotation_type, field_path, processor)

UserInfoArgs_validator = bv.Struct(UserInfoArgs)

class UserInfoError(bb.Struct):

    __slots__ = [
        '_err_value',
        '_error_message_value',
    ]

    _has_required_fields = False

    def __init__(self,
                 err=None,
                 error_message=None):
        self._err_value = bb.NOT_SET
        self._error_message_value = bb.NOT_SET
        if err is not None:
            self.err = err
        if error_message is not None:
            self.error_message = error_message

    # Instance attribute type: ErrUnion (validator is set below)
    err = bb.Attribute("err", nullable=True, user_defined=True)

    # Instance attribute type: str (validator is set below)
    error_message = bb.Attribute("error_message")

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(UserInfoError, self)._process_custom_annotations(annotation_type, field_path, processor)

UserInfoError_validator = bv.Struct(UserInfoError)

class UserInfoResult(bb.Struct):

    __slots__ = [
        '_family_name_value',
        '_given_name_value',
        '_email_value',
        '_email_verified_value',
        '_iss_value',
        '_sub_value',
    ]

    _has_required_fields = False

    def __init__(self,
                 family_name=None,
                 given_name=None,
                 email=None,
                 email_verified=None,
                 iss=None,
                 sub=None):
        self._family_name_value = bb.NOT_SET
        self._given_name_value = bb.NOT_SET
        self._email_value = bb.NOT_SET
        self._email_verified_value = bb.NOT_SET
        self._iss_value = bb.NOT_SET
        self._sub_value = bb.NOT_SET
        if family_name is not None:
            self.family_name = family_name
        if given_name is not None:
            self.given_name = given_name
        if email is not None:
            self.email = email
        if email_verified is not None:
            self.email_verified = email_verified
        if iss is not None:
            self.iss = iss
        if sub is not None:
            self.sub = sub

    # Instance attribute type: str (validator is set below)
    family_name = bb.Attribute("family_name", nullable=True)

    # Instance attribute type: str (validator is set below)
    given_name = bb.Attribute("given_name", nullable=True)

    # Instance attribute type: str (validator is set below)
    email = bb.Attribute("email", nullable=True)

    # Instance attribute type: bool (validator is set below)
    email_verified = bb.Attribute("email_verified", nullable=True)

    # Instance attribute type: str (validator is set below)
    iss = bb.Attribute("iss")

    # Instance attribute type: str (validator is set below)
    sub = bb.Attribute("sub")

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(UserInfoResult, self)._process_custom_annotations(annotation_type, field_path, processor)

UserInfoResult_validator = bv.Struct(UserInfoResult)

class ErrUnion(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    other = None

    @classmethod
    def auth_error(cls, val):
        """
        Create an instance of this class set to the ``auth_error`` tag with
        value ``val``.

        :param AuthError val:
        :rtype: ErrUnion
        """
        return cls('auth_error', val)

    def is_auth_error(self):
        """
        Check if the union tag is ``auth_error``.

        :rtype: bool
        """
        return self._tag == 'auth_error'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def get_auth_error(self):
        """
        Only call this if :meth:`is_auth_error` is true.

        :rtype: AuthError
        """
        if not self.is_auth_error():
            raise AttributeError("tag 'auth_error' not set")
        return self._value

    def _process_custom_annotations(self, annotation_type, field_path, processor):
        super(ErrUnion, self)._process_custom_annotations(annotation_type, field_path, processor)

ErrUnion_validator = bv.Union(ErrUnion)

AuthError._invalid_token_validator = bv.Void()
AuthError._no_openid_auth_validator = bv.Void()
AuthError._other_validator = bv.Void()
AuthError._tagmap = {
    'invalid_token': AuthError._invalid_token_validator,
    'no_openid_auth': AuthError._no_openid_auth_validator,
    'other': AuthError._other_validator,
}

AuthError.invalid_token = AuthError('invalid_token')
AuthError.no_openid_auth = AuthError('no_openid_auth')
AuthError.other = AuthError('other')

UserInfoArgs._all_field_names_ = set([])
UserInfoArgs._all_fields_ = []

UserInfoError.err.validator = bv.Nullable(ErrUnion_validator)
UserInfoError.error_message.validator = bv.String()
UserInfoError._all_field_names_ = set([
    'err',
    'error_message',
])
UserInfoError._all_fields_ = [
    ('err', UserInfoError.err.validator),
    ('error_message', UserInfoError.error_message.validator),
]

UserInfoResult.family_name.validator = bv.Nullable(bv.String())
UserInfoResult.given_name.validator = bv.Nullable(bv.String())
UserInfoResult.email.validator = bv.Nullable(bv.String())
UserInfoResult.email_verified.validator = bv.Nullable(bv.Boolean())
UserInfoResult.iss.validator = bv.String()
UserInfoResult.sub.validator = bv.String()
UserInfoResult._all_field_names_ = set([
    'family_name',
    'given_name',
    'email',
    'email_verified',
    'iss',
    'sub',
])
UserInfoResult._all_fields_ = [
    ('family_name', UserInfoResult.family_name.validator),
    ('given_name', UserInfoResult.given_name.validator),
    ('email', UserInfoResult.email.validator),
    ('email_verified', UserInfoResult.email_verified.validator),
    ('iss', UserInfoResult.iss.validator),
    ('sub', UserInfoResult.sub.validator),
]

ErrUnion._auth_error_validator = AuthError_validator
ErrUnion._other_validator = bv.Void()
ErrUnion._tagmap = {
    'auth_error': ErrUnion._auth_error_validator,
    'other': ErrUnion._other_validator,
}

ErrUnion.other = ErrUnion('other')

UserInfoError.error_message.default = ''
UserInfoResult.iss.default = ''
UserInfoResult.sub.default = ''
ROUTES = {
}
