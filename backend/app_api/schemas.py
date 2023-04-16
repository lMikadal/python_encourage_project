from ninja import Schema

class EncourageSchema(Schema):
    encourage: str

class ErrorSchema(Schema):
    error: str