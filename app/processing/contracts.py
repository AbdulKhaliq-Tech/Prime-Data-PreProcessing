"""
Future DataFrame-processing service contracts.

CRITICAL SCOPE NOTE:
Phase 00 does not implement import, cleaning, transformation, extraction,
statistical analysis, visualization, conversion, mock data generation,
automation, API integration, or export logic. This module exists only to
define the *shape* of the shared in-memory dataset/session contract so that
later phases (starting with Phase 02 — Import, FR-01) can implement against
a stable interface without redesigning the state model.

Nothing in this file performs data processing. `NotImplementedError` is
raised deliberately anywhere a later phase must supply real behavior.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional
from uuid import uuid4


@dataclass
class DatasetState:
    """
    Contract describing the shared working-dataset state.

    One clear current working DataFrame/dataset is a permanent project rule.
    This dataclass is the agreed shape for tracking that dataset's identity
    and lineage across modules — it intentionally does not hold an actual
    pandas DataFrame in Phase 00.
    """

    dataset_id: str = field(default_factory=lambda: str(uuid4()))
    name: Optional[str] = None
    original_dataset_id: Optional[str] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    is_modified: bool = False
    row_count: Optional[int] = None
    column_count: Optional[int] = None


class DataFrameProcessingService(ABC):
    """
    Contract that future processing services (Cleaning FR-02, Customization
    FR-03, Extraction FR-04, Statistical Analysis FR-06, Automation FR-10,
    etc.) must implement.

    Phase 00 defines the interface only. Concrete implementations belong to
    the phase that owns each functional requirement, per the SRS FR
    traceability (see docs/architecture/overview.md for the canonical FR
    numbering used across this project).
    """

    @abstractmethod
    def get_state(self, dataset_id: str) -> DatasetState:
        """Return the current state descriptor for a dataset."""
        raise NotImplementedError(
            "DataFrameProcessingService.get_state is a Phase 00 contract "
            "placeholder and must be implemented by a later phase."
        )

    @abstractmethod
    def apply_operation(self, dataset_id: str, operation: dict[str, Any]) -> DatasetState:
        """
        Apply a processing operation and return the updated state.

        View-only operations (search/filter/sort/visibility/order in Data
        Preview) must NOT go through this method — they are presentation
        state, not dataset mutation, per the Master UI Guidelines.
        """
        raise NotImplementedError(
            "DataFrameProcessingService.apply_operation is a Phase 00 "
            "contract placeholder and must be implemented by a later phase."
        )
