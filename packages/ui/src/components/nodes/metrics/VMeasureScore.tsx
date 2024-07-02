import { Handle, Position } from "reactflow";
import { IconRulerMeasure } from "@tabler/icons-react";

export default function VMeasureScore() {
  return (
    <div className="group rounded border border-gray-3 bg-gray-5 hover:border-yellow">
      <div className="relative flex h-10 items-center space-x-2 p-3">
        <IconRulerMeasure
          className="text-gray-2 group-hover:text-yellow"
          size={20}
          stroke={1.5}
        />
        <div className="text-yellow">V-Measure Score</div>
        <Handle
          type="target"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-purple outline-offset-2 hover:!bg-white hover:outline hover:outline-purple"
          position={Position.Left}
        />
        <Handle
          type="source"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-yellow outline-offset-2 hover:!bg-white hover:outline hover:outline-yellow"
          position={Position.Right}
        />
      </div>
      <div className="flex h-10 items-center space-x-2 bg-gray-4 p-3">
        <label className="italic text-gray-1">beta</label>
        <input
          placeholder="1.0"
          className="nodrag w-20 rounded-sm border border-gray-3 bg-gray-5 px-2 text-gray-1 focus:outline-none focus:border-yellow hover:border-gray-1"
        ></input>
      </div>
    </div>
  );
}
