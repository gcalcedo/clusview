import { Handle, Position } from "reactflow";
import { IconRosetteDiscountCheck } from "@tabler/icons-react";

export default function GroundtruthExtractor() {
  return (
    <div className="group rounded border border-gray-3 bg-gray-5 hover:border-purple">
      <div className="relative flex h-10 items-center space-x-2 p-3">
        <IconRosetteDiscountCheck
          className="text-gray-2 group-hover:text-purple"
          size={20}
          stroke={1.5}
        />
        <div className="text-purple">Groundtruth Extractor</div>
        <Handle
          type="target"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-green outline-offset-2 hover:!bg-white hover:outline hover:outline-green"
          position={Position.Left}
        />
        <Handle
          type="source"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-purple outline-offset-2 hover:!bg-white hover:outline hover:outline-purple"
          position={Position.Right}
        />
      </div>
    </div>
  );
}
