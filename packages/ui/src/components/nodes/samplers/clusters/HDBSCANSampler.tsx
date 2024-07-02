import { Handle, Position } from "reactflow";
import { IconCircles } from "@tabler/icons-react";

export default function HDBSCANSampler() {
  return (
    <div className="group rounded border border-gray-3 bg-gray-5 hover:border-red">
      <div className="relative flex h-20 items-center space-x-2 p-3">
        <IconCircles
          className="text-gray-2 group-hover:text-red"
          size={20}
          stroke={1.5}
        />
        <div className="text-red">HDBSCAN Sampler</div>
        <Handle
          type="target"
          id="embeddings"
          className="!mx-[-1rem] !my-[-1.5rem] !h-2 !w-2 !rounded-sm !border-none !bg-blue outline-offset-2 hover:!bg-white hover:outline hover:outline-blue"
          position={Position.Left}
        />
        <Handle
          type="target"
          id="min_cluster_size"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-red outline-offset-2 hover:!bg-white hover:outline hover:outline-red"
          position={Position.Left}
        />
        <Handle
          type="target"
          id="min_samples"
          className="!mx-[-1rem] !my-[1.5rem] !h-2 !w-2 !rounded-sm !border-none !bg-red outline-offset-2 hover:!bg-white hover:outline hover:outline-red"
          position={Position.Left}
        />
        <Handle
          type="source"
          className="!bg-purple hover:outline-purple !mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none outline-offset-2 hover:!bg-white hover:outline"
          position={Position.Right}
        />
      </div>
    </div>
  );
}
