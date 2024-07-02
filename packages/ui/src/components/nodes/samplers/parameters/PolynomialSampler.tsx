import { Handle, Position } from "reactflow";
import { IconMathFunction } from "@tabler/icons-react";

export default function PolynomialSampler() {
  return (
    <div className="group rounded border border-gray-3 bg-gray-5 hover:border-red">
      <div className="relative flex h-10 items-center space-x-2 p-3">
        <IconMathFunction
          className="text-gray-2 group-hover:text-red"
          size={20}
          stroke={1.5}
        />
        <div className="text-red">Polynomial Sampler</div>
        <Handle
          type="source"
          className="!mx-[-1rem] !h-2 !w-2 !rounded-sm !border-none !bg-red outline-offset-2 hover:!bg-white hover:outline hover:outline-red"
          position={Position.Right}
        />
      </div>
    </div>
  );
}
