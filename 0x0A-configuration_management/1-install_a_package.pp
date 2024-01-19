# 1-install_a_package.pp

# Install Flask package using Puppet
# Requirements:
# - Install flask
# - Version must be 2.1.0

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
