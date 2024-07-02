"use client";

import React, { useCallback } from "react";
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  Edge,
  Node,
  BackgroundVariant,
} from "reactflow";
import "reactflow/dist/style.css";

import CSVLoader from "./nodes/loaders/documents/CSVLoader";
import GroundtruthExtractor from "./nodes/loaders/documents/GroundtruthExtractor";
import ColumnConcatenator from "./nodes/operators/dataframes/ColumnConcatenator";
import UMAP from "./nodes/operators/embeddings/UMAP";
import SilhouetteScore from "./nodes/metrics/SilhouetteScore";
import OutlierRatio from "./nodes/metrics/OutlierRatio";
import VMeasureScore from "./nodes/metrics/VMeasureScore";
import MetricMapper from "./nodes/metrics/MetricMapper";
import LinearSampler from "./nodes/samplers/parameters/LinearSampler";
import PolynomialSampler from "./nodes/samplers/parameters/PolynomialSampler";
import HDBSCANSampler from "./nodes/samplers/clusters/HDBSCANSampler";
import Transformer from "./nodes/transformers/Transformer";

const nodeTypes = {
  csvLoader: CSVLoader,
  groundtruthExtractor: GroundtruthExtractor,
  columnConcatenator: ColumnConcatenator,
  umap: UMAP,
  silhouetteScore: SilhouetteScore,
  outlierRatio: OutlierRatio,
  vMeasureScore: VMeasureScore,
  metricMapper: MetricMapper,
  linearSampler: LinearSampler,
  polynomialSampler: PolynomialSampler,
  hdbscanSampler: HDBSCANSampler,
  transformer: Transformer,
};

const initialNodes: Node[] = [
  {
    id: "1",
    type: "csvLoader",
    position: { x: 0, y: 0 },
    data: {},
  },
  {
    id: "2",
    type: "columnConcatenator",
    position: { x: 0, y: 60 },
    data: {},
  },
  {
    id: "3",
    type: "transformer",
    position: { x: 0, y: 120 },
    data: {},
  },
  {
    id: "4",
    type: "umap",
    position: { x: 0, y: 180 },
    data: {},
  },
  {
    id: "5",
    type: "linearSampler",
    position: { x: 0, y: 240 },
    data: {},
  },
  {
    id: "6",
    type: "polynomialSampler",
    position: { x: 0, y: 300 },
    data: {},
  },
  {
    id: "7",
    type: "hdbscanSampler",
    position: { x: 0, y: 360 },
    data: {},
  },
  {
    id: "8",
    type: "silhouetteScore",
    position: { x: 0, y: 460 },
    data: {},
  },
  {
    id: "9",
    type: "outlierRatio",
    position: { x: 0, y: 520 },
    data: {},
  },
  {
    id: "10",
    type: "metricMapper",
    position: { x: 0, y: 580 },
    data: {},
  },
  {
    id: "11",
    type: "vMeasureScore",
    position: { x: 0, y: 680 },
    data: {},
  },
  {
    id: "12",
    type: "groundtruthExtractor",
    position: { x: 0, y: 780 },
    data: {},
  }
];

export default function ClusviewFlow() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  const onConnect = useCallback(
    (connection: Edge | Connection) =>
      setEdges((eds) => addEdge({ ...connection }, eds)),
    [setEdges],
  );

  return (
    <div className="h-full w-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        snapToGrid
        snapGrid={[20, 20]}
        defaultEdgeOptions={{ animated: true }}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        onInit={(reactFlowInstance) => {
          reactFlowInstance.fitView();
          reactFlowInstance.zoomTo(1);
        }}
      >
        <Controls />
        <MiniMap />
        <Background variant={BackgroundVariant.Dots} gap={20} size={1} />
      </ReactFlow>
    </div>
  );
}
