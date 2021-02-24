from dwave.system import EmbeddingComposite, DWaveSampler
from dimod.binary_quadratic_model import BinaryQuadraticModel


#Q = {(-17, 6, 8, 10, 12)
#     (0, -30, 14, 18, 22)
#     (0, 0, -41, 26, 32)
#     (0, 0, 0, -50, 42)
#     (0, 0, 0, 0, -57)}

Q = {('x1', 'x1') : -20,
     ('x1', 'x2') : 6,
     ('x1', 'x3') : 8,
     ('x1', 'x4') : 10,
     ('x1', 'x5') : 12,
     ('x2', 'x2') : -33,
     ('x2', 'x3') : 14,
     ('x2', 'x4') : 18,
     ('x2', 'x5') : 22,
     ('x3', 'x3') : -44,
     ('x3', 'x4') : 26,
     ('x3', 'x5') : 32,
     ('x4', 'x4') : -53,
     ('x4', 'x5') : 42,
     ('x5', 'x5') : -60,
     }

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_qubo(Q,
                                 num_reads = 10,
                                 label='Example - Simple Ocean Programs: QUBO')
print(sampleset)
