from schemas.aluguel import Aluguel, AluguelViewSchema, AluguelRequestSchema, \
                            AluguelGetSchema, AluguelPostFormSchema, \
                            AluguelPutFormSchema, AluguelPutPathSchema, \
                            AluguelDeleteSchema, AluguelDeleteViewSchema, \
                            ListaAlugueisSchema, \
                            show_aluguel, show_alugueis

from schemas.cliente import Cliente, ClienteBuscaPorCpfHeaderSchema, ClienteDeleteSchema, ClienteDeleteViewSchema, \
                            ClienteGetSchema, ClienteGetPorCpfSchema, ClientePostSchema, ClientePutSchema, \
                            ClienteViewSchema, ListaClientesSchema, \
                            show_cliente, show_clientes

from schemas.veiculo import VeiculoViewSchema, ListaVeiculosSchema, show_veiculos

from schemas.error import ErrorSchema
