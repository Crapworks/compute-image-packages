#!/usr/bin/python
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities that are distro specific."""


class Utils(object):
  """Utilities used by Linux guest services."""

  def __init__(self, debug=False):
    """Constructor.

    Args:
      debug: bool, True if debug output should write to the console.
    """
    self.debug = debug

  def EnableIpv6(self, interfaces, logger, dhclient_script=None):
    """Enable IPv6 on the list of network interfaces.

    Args:
      interfaces: list of string, the output device names for enabling IPv6.
      logger: logger object, used to write to SysLog and serial port.
      dhclient_script: string, the path to a dhclient script used by dhclient.
    """
    pass

  def DisableIpv6(self, interfaces, logger):
    """Disable Ipv6.

    Args:
      interface: string, the output device names for enabling IPv6.
      logger: logger object, used to write to SysLog and serial port.
    """
    pass

  def EnableNetworkInterfaces(self, interfaces, logger, dhclient_script=None):
    """Enable the list of network interfaces.

    Args:
      interfaces: list of string, the output device names to enable.
      logger: logger object, used to write to SysLog and serial port.
      dhclient_script: string, the path to a dhclient script used by dhclient.
    """
    pass

  def ChangeDefaultRoute(self, defaultgw, interface, source_ip, logger):
    """Change the default route to set an explicit source ip.

    Args:
      defaultgw: string, address of the default gateway.
      interface: string, name of the interface.
      source_ip: string, source ip of the default route.
      logger: logger object, used to write to SysLog and serial port.
    """
    pass

  def HandleClockSync(self, logger):
    """Sync the software clock with the hypervisor clock.

    Args:
      logger: logger object, used to write to SysLog and serial port.
    """
    pass

  def IpForwardingUtils(self, logger, proto_id=None):
    """Get system IP address configuration utilities.

    Args:
      logger: logger object, used to write to SysLog and serial port.
      proto_id: string, the routing protocol identifier for Google IP changes.
    """
    pass
