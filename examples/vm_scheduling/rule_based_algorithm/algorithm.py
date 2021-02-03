import math

from maro.simulator.scenarios.vm_scheduling.common import Action
from maro.simulator.scenarios.vm_scheduling import AllocateAction, DecisionPayload, PostponeAction


class VMSchedulingAgent(object):
    def choose_action(self, decision_event: DecisionPayload, env: Env) -> Action:
        """This method will determine whether to postpone the current VM or allocate a PM to the current VM.
        """
        valid_pm_num: int = len(decision_event.valid_pms)

        if valid_pm_num <= 0:
            # No valid PM now, postpone.
            action: PostponeAction = PostponeAction(
                vm_id=decision_event.vm_id,
                postpone_step=1
        else:
            action: AllocateAction = self.allocate_vm(decision_event, env)

        return action

    def allocate_vm(self, decision_event: DecisionPayload, env: Env) -> AllocateAction:
        """This method will determine allocate which PM to the current VM.
        """
        pass
