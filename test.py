from qistik  import QuantumCircuit, transpile
from qistik_aer import AerSimulator
from qistik.visualization import plot_histogram

QuantumCircuit(2, 2) #circuito com 2qubits e 2bits classicos

qc.h(0) #Hardamard

qc.cx(0, 1) #CNOT

qc.measure([0, 1], [0, 1])

simulator = AerSimulator()
compile_circuit = transpile(qc, simulator)
job = simulator.run(compile_circuit, shosts=1000)

result = job.result()
counts = result.get_counts(qc)
print("\ncontagem dos resultados:", counts)

plot_histogram(counts)

