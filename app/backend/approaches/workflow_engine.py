"""
workflow_engine.py
Reusable workflow engine for agent-driven audit automation.
"""

from typing import Any, Callable, Dict, List

class WorkflowEngine:
    def __init__(self):
        pass

    def run_workflow(self, steps: List[Callable], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a sequence of workflow steps, passing context between them.
        Each step is a callable that takes and returns context.
        """
        for step in steps:
            context = step(context)
        return context

    @staticmethod
    def retrieval_step(retriever: Callable, context: Dict[str, Any]) -> Dict[str, Any]:
        context['documents'] = retriever(context)
        return context

    @staticmethod
    def context_assembly_step(assembler: Callable, context: Dict[str, Any]) -> Dict[str, Any]:
        context['assembled_context'] = assembler(context)
        return context

    @staticmethod
    def prompt_rendering_step(renderer: Callable, context: Dict[str, Any]) -> Dict[str, Any]:
        context['prompt'] = renderer(context)
        return context

    @staticmethod
    def ai_call_step(ai_caller: Callable, context: Dict[str, Any]) -> Dict[str, Any]:
        context['ai_response'] = ai_caller(context)
        return context

# Example usage in agent modules:
# steps = [WorkflowEngine.retrieval_step, WorkflowEngine.context_assembly_step, WorkflowEngine.prompt_rendering_step, WorkflowEngine.ai_call_step]
# result = WorkflowEngine().run_workflow(steps, context)
