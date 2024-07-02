import { Handle, Position } from "reactflow";
import { IconMap } from "@tabler/icons-react";

export default function MetricMapper() {
  return (
    <div className="hover:border-purple group rounded border border-gray-3 bg-gray-5">
      <div className="relative flex h-20 items-center space-x-2 p-3">
        <IconMap
          className="group-hover:text-purple text-gray-2"
          size={20}
          stroke={1.5}
        />
        <div className="text-purple">Metric Mapper</div>
        <Handle
          type="target"
          id="clustering"
          className="!bg-purple hover:outline-purple !mx-[-1rem] !my-[-1.7rem] !h-2 !w-2 !rounded-sm !border-none outline-offset-2 hover:!bg-white hover:outline"
          position={Position.Left}
        />
        <Handle
          type="target"
          id="metric_1"
          className="!mx-[-1rem] !my-[-0.55rem] !h-2 !w-2 !rounded-sm !border-none !bg-yellow outline-offset-2 hover:!bg-white hover:outline hover:outline-yellow"
          position={Position.Left}
        />
        <Handle
          type="target"
          id="metric_2"
          className="!mx-[-1rem] !my-[0.55rem] !h-2 !w-2 !rounded-sm !border-none !bg-yellow outline-offset-2 hover:!bg-white hover:outline hover:outline-yellow"
          position={Position.Left}
        />
        <Handle
          type="target"
          id="metric_3"
          className="!mx-[-1rem] !my-[1.7rem] !h-2 !w-2 !rounded-sm !border-none !bg-yellow outline-offset-2 hover:!bg-white hover:outline hover:outline-yellow"
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
