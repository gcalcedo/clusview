import { Handle, Position } from "reactflow";
import { IconBrain } from "@tabler/icons-react";

export default function Transformer() {
  return (
    <div className="group rounded border border-gray-3 bg-gray-5 hover:border-blue">
      <div className="relative flex h-10 items-center space-x-2 p-3">
        <IconBrain
          className="text-gray-2 group-hover:text-blue"
          size={20}
          stroke={1.5}
        />
        <div className="text-blue">Transformer</div>
        <Handle
          type="target"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-green outline-offset-2 hover:!bg-white hover:outline hover:outline-green"
          position={Position.Left}
        />
        <Handle
          type="source"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-blue outline-offset-2 hover:!bg-white hover:outline hover:outline-blue"
          position={Position.Right}
        />
      </div>
    </div>
  );
}
