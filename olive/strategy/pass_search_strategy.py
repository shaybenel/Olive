# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------
import copy
from typing import Any, Dict, List, Optional, OrderedDict


class PassSearchStrategy:
    """Search strategy implementation to generate/iterate all permutations."""

    def __init__(self, pass_configs: OrderedDict[str, List[Dict[str, Any]]]):
        self.pass_configs = pass_configs

        self.suggestions = []
        for name, configs in pass_configs.items():
            if self.suggestions:
                suggestions = self.suggestions
                self.suggestions = [
                    OrderedDict([*suggestion.items(), (name, config)])
                    for config in configs
                    for suggestion in copy.deepcopy(suggestions)
                ]
            else:
                self.suggestions = [OrderedDict([(name, config)]) for config in configs]

        self.next_suggestion = 0

    def next_step(self) -> Optional[OrderedDict[str, Any]]:
        if self.next_suggestion >= len(self.suggestions):
            return None

        suggestion = self.suggestions[self.next_suggestion]
        self.next_suggestion += 1
        return suggestion
