import attrs


@attrs.define
class TrainingSessionCreated:
    training_session_id: str
