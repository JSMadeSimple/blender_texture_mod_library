import bpy
element = bpy.context.active_object
neon = bpy.data.materials.new("red")
element.data.materials.append(neon)
neon.use_nodes=True
nodes = neon.node_tree.nodes
material_output=nodes.get("Material Output")
node_emission=nodes.new(type='ShaderNodeEmission')
node_emission.inputs[0].default_value=(0.0, 0.9, 1.0, 0)
node_emission.inputs[1].default_value=500

#linker between the shaders
linker=neon.node_tree.links
linker.new(node_emission.outputs[0],material_output.inputs[0])
