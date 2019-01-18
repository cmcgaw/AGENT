import itertools

from FlowExecution.PlannedTestFlow import PlannedTestFlow


class FlowPlanner:
    def __init__(self, logger, aide):
        self.log = logger
        self.aide = aide
        self._klass = __class__.__name__

    def plan(self, context, act_state, page_analysis, flow):
        planned_flows = []

        plan_steps = []

        for action in flow.act.actions:
            if action.action == 'TRY':
                widget = act_state.find_widget_with_label(action.component.ident, 'set')

                if not widget:
                    self.log.Error(context, self._klass, "execute", "Unable to bind flow act step: " + str(action))
                    return False

                plan_steps.append([(action, widget)])

            elif action.action == 'CLICK':
                element_class = action.equivalence_class.element_class

                if element_class is None and action.equivalence_class.ident is not None:
                    element_class = action.equivalence_class.ident

                if element_class not in page_analysis['analysis']:
                    self.log.Error(context, self._klass, "execute", "Unable to bind flow act step: " + str(action))
                    return False

                candidate_widgets = page_analysis['analysis'][element_class]

                possible_steps = []

                for candidate_widget_key in candidate_widgets:
                    if candidate_widget_key not in act_state.widget_map or 'click' not in act_state.widget_map[candidate_widget_key]['actions']:
                        continue

                    actual_widget = act_state.widget_map[candidate_widget_key]

                    possible_steps.append((action, actual_widget))

                plan_steps.append(possible_steps)

        cartesian_product = itertools.product(*plan_steps)

        for seq in cartesian_product:
            planned_flows.append(PlannedTestFlow(None, act_state, flow, seq))

        return planned_flows


