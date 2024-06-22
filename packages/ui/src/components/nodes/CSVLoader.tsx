import { Handle, Position } from "reactflow";
import { IconTablePlus } from "@tabler/icons-react";

export default function CSVLoader() {
  return (
    <div className="bg-gray-5 border-gray-3 hover:border-green border rounded group">
      <div className="flex space-x-2 p-3 items-center relative h-10">
        <IconTablePlus
          className="text-gray-2 group-hover:text-green"
          size={20}
          stroke={1.5}
        />
        <div className="text-green">CSV Loader</div>
        <Handle
          type="source"
          className="!rounded-sm hover:outline-green hover:!bg-white !w-2 !h-2 !bg-green !mx-[-1rem] outline-offset-2 hover:outline !border-none"
          position={Position.Right}
        />
      </div>
    </div>
  );
}
