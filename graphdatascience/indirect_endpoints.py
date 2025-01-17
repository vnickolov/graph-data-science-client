from .algo.algo_endpoints import AlgoEndpoints
from .graph.graph_endpoints import GraphEndpoints
from .model.model_endpoints import ModelEndpoints
from .pipeline.pipeline_endpoints import PipelineEndpoints
from .query_runner.query_runner import QueryRunner
from .similarity.similarity_endpoints import SimilarityEndpoints
from .system.system_endpoints import SystemEndpoints
from .topological_lp.topological_lp_endpoints import TopologicalLPEndpoints
from .utils.util_endpoints import UtilEndpoints


class IndirectEndpoints(
    AlgoEndpoints,
    GraphEndpoints,
    ModelEndpoints,
    PipelineEndpoints,
    SystemEndpoints,
    TopologicalLPEndpoints,
    UtilEndpoints,
    SimilarityEndpoints,
):
    def __init__(self, query_runner: QueryRunner, namespace: str):
        super().__init__(query_runner, namespace)
