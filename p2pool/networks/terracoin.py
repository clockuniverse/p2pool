from p2pool.bitcoin import networks

PARENT = networks.nets['terracoin']
SHARE_PERIOD = 45 # seconds
CHAIN_LENGTH = 24*60*60//30 # shares
REAL_CHAIN_LENGTH = 24*60*60//30 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 10 # blocks
IDENTIFIER = 'a42a265ad1b6d42b'.decode('hex')
PREFIX = '56a3f62173d2a9b5'.decode('hex')
P2P_PORT = 9323
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 9322
BOOTSTRAP_ADDRS = 'terracoinpool.ddns.net p2p.hashpool.eu trc.multicoin.co'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: 91201 <= v
VERSION_WARNING = lambda v: 'Upgrade Terracoin to >= 0.9.12.1!' if v < 91201 else None
