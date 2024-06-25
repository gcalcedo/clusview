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
import CSVLoader from "./nodes/loaders/documents/CSVLoader";

import "reactflow/dist/style.css";

const initialNodes: Node[] = [
  {
    id: "1",
    type: "csvLoader",
    position: { x: 0, y: 0 },
    data: {},
  },
];

const nodeTypes = { csvLoader: CSVLoader };

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
