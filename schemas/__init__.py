from schemas.aluguel import Aluguel, AluguelViewSchema, AluguelDeleteViewSchema,  AluguelRequestSchema, \
                            AluguelGetSchema, AluguelPostSchema, AluguelPutSchema, AluguelDeleteSchema, \
                            ListaAlugueisSchema, \
                            show_aluguel, show_alugueis

from schemas.cliente import Cliente, ClienteBuscaPorCpfHeaderSchema, ClienteDeleteSchema, ClienteDeleteViewSchema, \
                            ClienteGetSchema, ClienteGetPorCpfSchema, ClientePostSchema, ClientePutSchema, \
                            ClienteViewSchema, ListaClientesSchema, \
                            show_cliente, show_clientes

from schemas.veiculo import VeiculoViewSchema, ListaVeiculosSchema, show_veiculos

from schemas.error import ErrorSchema
