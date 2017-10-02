
import datetime
import logging
import wishful_controller
import gevent
import wishful_upis as upis

log = logging.getLogger('wishful_controller')
log_level = logging.INFO
logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s.%(funcName)s() - %(levelname)s - %(message)s')

#Create controller
controller = wishful_controller.Controller()

controller.set_controller_info(name="WishfulController", info="WishfulControllerInfo")
controller.add_module(moduleName="ibfd_agent", pyModuleName="IBFD_agent",
                      className="IBFDAgent")

#start the radio
controller.run()

#set parameters
controller.radio.iface("usrp0").set_parameters({'SELF_INT':True})
controller.radio.iface("usrp0").set_parameters({'RETUNE_DUPLEXER':True})

controller.radio.iface("usrp0").set_parameters({'SET_CD':'reset'})
time.sleep(2)
print('... Training')
controller.radio.iface("usrp0").set_parameters({'SET_CD':'train'})
time.sleep(4)
print('... Fix Alpha')
controller.radio.iface("usrp0").set_parameters({'SET_CD':'fix_alpha'})
time.sleep(2)
print('... Start CD')
controller.radio.iface("usrp0").set_parameters({'SET_CD':'start'})
time.sleep(3)
