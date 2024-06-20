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

const initialNodes: Node[] = [
  { id: "1", position: { x: 0, y: 0 }, data: { label: "Source" } },
  { id: "2", position: { x: 60, y: 160 }, data: { label: "Target" } },
];
const initialEdges: Edge[] = [{ id: "e1-2", source: "1", target: "2" }];

export default function ClusviewFlow() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (connection: Edge | Connection) =>
      setEdges((eds) => addEdge({ ...connection }, eds)),
    [setEdges]
  );

  return (
    <div className="w-full h-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        snapToGrid
        snapGrid={[20, 20]}
        defaultEdgeOptions={{ animated: true }}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onInit={(reactFlowInstance) => reactFlowInstance.fitView()}
      >
        <Controls />
        <MiniMap />
        <Background variant={BackgroundVariant.Dots} gap={20} size={1} />
      </ReactFlow>
    </div>
  );
}
