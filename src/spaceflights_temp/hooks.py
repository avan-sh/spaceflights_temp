from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline, node
from typing import Dict, Any
from kedro.framework.context import KedroContext
import time


class ProjectHooks:
    # @hook_impl
    # def after_context_created(
    #     self,
    #     context: KedroContext,
    # ):
    #     print(context.__dict__)
    #     pass

    # @hook_impl
    # def before_pipeline_run(
    #     self, run_params: Dict[str, Any], pipeline: Pipeline, catalog: DataCatalog
    # ) -> None:
    #     dummy_node = node(simple_log, inputs=None, outputs="hello")
    #     pipeline = Pipeline([dummy_node])
    #     pass

    @hook_impl
    def before_node_run(self, node: node, catalog, inputs, is_async, session_id):
        if node.name == "simple_log":
            loaded_datasets = [
                catalog.load(dataset) for dataset in inputs["params:log_inputs"]
            ]
            inputs["params:log_inputs"] = loaded_datasets
            return inputs
        pass

    # @hook_impl
    # def before_node_run(self, node: node, catalog, inputs, is_async, session_id):
    #     if node.name == "simple_log":
    #         loaded_datasets = [
    #             catalog.load(dataset) for dataset in inputs["params:log_inputs"]
    #         ]
    #         inputs["params:log_inputs"] = loaded_datasets
    #         return inputs
    #     pass
