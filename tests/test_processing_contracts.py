"""
Future DataFrame test fixtures/mocks — Phase 00 foundation testing requirement.

These tests confirm the *shape* of the shared dataset-state contract that
later phases (Import FR-01, Cleaning FR-02, etc.) will implement against.
No business processing logic is tested or implemented here.
"""

import pytest

from app.processing.contracts import DataFrameProcessingService, DatasetState


def test_dataset_state_has_expected_default_shape():
    state = DatasetState(name="sample.csv")
    assert state.dataset_id
    assert state.name == "sample.csv"
    assert state.is_modified is False
    assert state.original_dataset_id is None


class _StubProcessingService(DataFrameProcessingService):
    """Minimal stub used only to prove the abstract contract is implementable."""

    def get_state(self, dataset_id: str) -> DatasetState:
        return DatasetState(dataset_id=dataset_id)

    def apply_operation(self, dataset_id: str, operation: dict) -> DatasetState:
        return DatasetState(dataset_id=dataset_id, is_modified=True)


def test_contract_is_implementable_by_a_future_phase():
    service = _StubProcessingService()
    state = service.get_state("abc-123")
    assert state.dataset_id == "abc-123"

    updated = service.apply_operation("abc-123", {"op": "noop"})
    assert updated.is_modified is True


def test_abstract_service_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        DataFrameProcessingService()
