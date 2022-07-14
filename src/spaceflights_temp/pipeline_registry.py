"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, node

from spaceflights_temp.pipelines import data_processing as dp
from spaceflights_temp.pipelines import data_science as ds
from spaceflights_temp.pipelines.data_processing.nodes import simple_log


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    simple_pipe = Pipeline(
        [
            node(
                func=simple_log,
                inputs="params:log_inputs",
                outputs=None,
                name="preprocess_companies_node",
            ),
        ]
    )

    return {
        "__default__": simple_pipe,
        # data_processing_pipeline  + data_science_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
    }
