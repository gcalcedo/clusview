import { Handle, Position } from "reactflow";
import { IconRulerMeasure } from "@tabler/icons-react";

export default function OutlierRatio() {
  return (
    <div className="group rounded border border-gray-3 bg-gray-5 hover:border-yellow">
      <div className="relative flex h-10 items-center space-x-2 p-3">
        <IconRulerMeasure
          className="text-gray-2 group-hover:text-yellow"
          size={20}
          stroke={1.5}
        />
        <div className="text-yellow">Outlier Ratio</div>
        <Handle
          type="source"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-yellow outline-offset-2 hover:!bg-white hover:outline hover:outline-yellow"
          position={Position.Right}
        />
      </div>
    </div>
  );
}
