import { Handle, Position } from "reactflow";
import { IconTablePlus } from "@tabler/icons-react";

export default function CSVLoader() {
  return (
    <div className="bg-[#252D3E] border-[#4d5b7a] hover:border-[#36E7A7] border rounded group">
      <div className="flex space-x-2 p-3 items-center relative h-10">
        <IconTablePlus className="text-[#65769c] group-hover:text-[#36E7A7]" size={20} stroke={1.5} />
        <div className="text-[#36E7A7]">CSV Loader</div>
        <Handle
          type="source"
          className="!rounded-sm hover:outline-[#36E7A7] hover:!bg-[#E3E7F5] !w-2 !h-2 !bg-[#36E7A7] !mx-[-1rem] outline-offset-2 hover:outline !border-none"
          position={Position.Right}
        />
      </div>
    </div>
  );
}
