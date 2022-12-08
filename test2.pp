# Create two users.
$users = ['user1', 'user2']

user { $users:
  ensure  => present,
  groups  => ['my_group']
}

# Create group.
group { 'my_group':
  ensure => present
}

# Install packages.
package { 'python':
  ensure => installed,
  provider => pip3
}

# python3 --version

package {'pip3':
  require  => Package['python3-pip'],
  ensure   => installed,
  provider => 'pip3'
}
# pip3 --version

$packages = ['python3-pip', 'apache2', 'libapache2-mod-wsgi']

package { $packages:
  ensure => installed
}
# /usr/sbin/apache2 -v
# dpkg -s libapache2-mod-wsgi

package { bottle:
  ensure   => '0.10.11',
  provider => 'pip3',
  require  => Package['libapache2-mod-wsgi']
}
# python3 -m bottle --version
